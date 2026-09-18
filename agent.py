from trajectory import Trajectory
from llm import LLM

class TinyAgent:

    def __init__(self,llm:LLM):
        self.llm = llm
        self.memory = None
        self.tools = None
        self.planner = None

        self.trajectory = Trajectory()

        
    def run(self,task:str) -> str:
        self.trajectory.initialize(task)
        return self._step(task)

    def _step(self,task:str) -> str:
        messages = [{"role": "user", "content": task}]
        response = self.llm.generate(messages)
        self.trajectory.add_step(response)
        return response.content

    def _execute_action(self,action:str) -> str:
        return f"Executed: {action}"