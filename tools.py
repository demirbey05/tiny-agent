from typing import Callable


def multiply(a: str, b: str) -> float:
    return float(a) * float(b)

class Tools:

    def __init__(self,requires_approval: list[str] = []) -> None:
        self.requires_approval = requires_approval
        self.registry = dict()
    

    def add_tool(self,name:str,func:Callable,description:str= "") -> None:

        self.registry[name] = {"function":func,"description":description}

    @property
    def schemas(self) ->None:
        return None
    

    @property
    def descriptions(self) -> str:
        """Get descriptions of all registered tools."""
        return "\n".join(
            f"`{tool}`: {self.registry[tool]['description']}"
            for tool in self.registry
        )
 
    @property
    def prompt(self) -> str:
        return f"""
# Tools
If needed, you can only use the following tools to assist you 
in completing tasks:


{self.descriptions}


To use a tool, respond with JSON: 
{{"tool": "name", "kwargs": {{"param": "value"}}}}
"""