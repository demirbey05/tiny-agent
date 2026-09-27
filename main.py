from rag import RAGMemory
from llm import LLM, Response
from agent import TinyAgent
from memory import Memory, TrimmingMemory
from embedding import EmbeddingModel


def run_local_llm():
    documents = [
        "Sarah works as a marine biologist studying coral reefs.",
        "Sarah lives in Lisbon, Portugal.",
        "Sarah's favorite hobby is rock climbing.",
        "Sarah favorite animal is flamingos.",
        "Sarah speaks fluent Spanish and Portuguese.",
        "Ilse is a software engineer at a renewable energy startup.",
        "Ilse lives in Amsterdam, the Netherlands.",
        "Ilse plays the cello in a local string quartet.",
        "Ilse's favorite author is Brandon Sanderson.",
        "Ilse's favorite animal is dolphins.",
    ]

    # Load the embedding model
    embedding_model = EmbeddingModel(model="embeddinggemma")
    
    # Create RAGMemory
    rag_memory = RAGMemory(documents=documents, embedding_model=embedding_model)

    # Initialize the LLM
    llm = LLM(model="gemma3:12b")

    # Create the Agent and run a query
    agent = TinyAgent(llm=llm, memory=rag_memory)
    response = agent.run("What is Sarah's favorite animal?")
    print(response)
    print(agent.memory.get_messages())

if __name__ == "__main__":
    run_local_llm()

