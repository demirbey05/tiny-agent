from dataclasses import dataclass


@dataclass
class Step:

    thought:str = "" # Agent's reasoning process to form answer
    action : str | None = None # The name of tool call if exists
    observation :str | None = None # Result of tool call if exists
    metadata :dict | None = None # Additional metadata
    answer:str | None =None # Final answer if exists(might be only tool call)




class Trajectory:

    def __init__(self):
        self.runs:list[dict] = []
    
    def initialize(self,query:str) -> None:
        self.runs.append({
            "query":query,
            "steps":[]
        })
    
    def add_step(self,response,observation:str|None = None):
        step = Step(
            thought= response.reasoning or "",
            metadata= response.metadata
        )
        
        
        if observation is not None:
            step.action = response.tool_call
            step.observation = observation
        else:
            step.answer = response.content
        self.runs[-1]["steps"].append(step)

        
            