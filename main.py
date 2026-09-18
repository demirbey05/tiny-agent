from illustrated_agents.utils import TrajectoryViewer
from llm import LLM,Response
from agent import TinyAgent


def run_local_llm():
    # Re-initialize the LLM with the updated class
    llm = LLM(model="gemma3:12b")
    agent = TinyAgent(llm=llm)
    response = agent.run("What is 2 + 2?")
    TrajectoryViewer(agent.trajectory)


if __name__ == "__main__":
    run_local_llm()
