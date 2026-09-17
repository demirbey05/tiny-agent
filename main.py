from llm import LLM,Response


def run_local_llm():
    # Re-initialize the LLM with the updated class
    llm = LLM(model="gemma3:12b")
 
    # Generate a `Response` dataclass
    response = llm.generate([{"role": "user", "content": "Hi! How's life?"}])
    print(response)


if __name__ == "__main__":
    run_local_llm()
