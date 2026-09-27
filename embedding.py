import urllib.request
import json

class EmbeddingModel:

    def __init__(self,model:str,base_url:str = "http://localhost:11434/v1"):
        self.model = model
        self.base_url = base_url
        

    def embed(self,text:str) -> list[float]:

        request = urllib.request.Request(
            f"{self.base_url}/embeddings",
            data=json.dumps({"model": self.model, "input": text}).encode(),
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(request) as resp:
            response = json.loads(resp.read())
 
        return response["data"][0]["embedding"]
        

