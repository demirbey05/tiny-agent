from __future__ import annotations
from llm import LLM


class Memory:
    def __init__(self):
        self.messages = []

    def add(self, role: str, content: str, tool_call: dict | None = None) -> None:
        msg = {"role": role, "content": content}
        if tool_call:
            msg["tool_call"] = tool_call
        self.messages.append(msg)

    def get_messages(self) -> list[dict]:
        return self.messages


class TrimmingMemory(Memory):
    def __init__(self, last_k: int = 4):
        super().__init__()
        self.last_k = last_k

    def add(self, role: str, content: str, **kwargs) -> None:
        super().add(role, content, **kwargs)

        system = [message for message in self.messages if message.get("role") == "system"]
        non_system = [message for message in self.messages if message.get("role") != "system"]

        self.messages = system + non_system[-self.last_k:]


class SummarizationMemory(Memory):
    """Memory that compresses past turns into a running summary via an LLM."""

    def __init__(self, llm: LLM):
        super().__init__()
        self.llm = llm

    def add(self, role: str, content: str, **kwargs) -> None:
        # Add the new message first using the parent class (Memory)
        super().add(role, content, **kwargs)

        # After each completed turn, update the running summary
        if role in ("assistant", "asisstant"):
            # Split the existing summary from the new conversation turns
            summary = ""
            conversation = ""
            for message in self.messages:
                if message["role"] == "system":
                    summary = message["content"]
                else:
                    conversation += f"{message['role']}: {message['content']}\n"

            # Ask the LLM to extend the summary with the new conversation
            prompt = f"""Update the summary with the new conversation.

Summary: {summary}

Conversation:
{conversation}
Output the updated summary only."""
            response = self.llm.generate([{"role": "user", "content": prompt}])
            self.messages = [{"role": "system", "content": response.content}]