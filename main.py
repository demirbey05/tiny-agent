import memory
import llm
from llm import LLM,Response
from agent import TinyAgent
from memory import Memory,TrimmingMemory


def run_local_llm():
    # Re-initialize the LLM with the updated class
    llm = LLM(model="gemma3:12b")
    memory = TrimmingMemory()
    agent = TinyAgent(llm=llm, memory=memory)
 
    # Run some interactions
    response_1 = agent.run("Hi! I'm reading 'An Illustrated Guide to AI Agents'.")
    response_2 = agent.run("There are many flamingos in this book, why?")
    response_3 = agent.run("What is 1+1?")
    response_4 = agent.run("What is 2+2?")

    print(agent.memory.get_messages())

if __name__ == "__main__":
    run_local_llm()
