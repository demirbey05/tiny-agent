from tools import Tools,multiply

def run_local_llm():

    tools = Tools()
    
    tools.add_tool("multiply", multiply, "Multiplies two numbers: multiply(a: str, b: str)")
    
    print(tools.prompt)
    
    pass
    

if __name__ == "__main__":
    run_local_llm()

