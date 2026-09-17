class TinyAgent:

    def __init__(self):
        self.llm = None
        self.memory = None
        self.tools = None
        self.planner = None

    

    def run(self,task:str) -> str:
        return self._step(task)

    def _step(self,task:str) -> str:
        return f"Received: {task}"

    def _execute_action(self,action:str) -> str:
        return f"Executed: {action}"