from trajectory import Trajectory
from llm import LLM
from memory import Memory

class TinyAgent:

    def __init__(self,llm:LLM,memory:Memory):
        self.llm = llm
        self.memory = memory
        self.tools = None
        self.planner = None

        self.trajectory = Trajectory()

        
    def run(self,task:str) -> str:
        self.memory.add("user",task)
        self.trajectory.initialize(task)
        return self._step()

    def _step(self) -> str:
        response = self.llm.generate(self.memory.get_messages())
        self.memory.add("assistant",response.content,tool_call=response.tool_call)
        self.trajectory.add_step(response)
        return response.content

    def _execute_action(self,action:str) -> str:
        return f"Executed: {action}"