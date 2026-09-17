from dataclasses import dataclass
import urllib.request
import json

@dataclass
class Response:

    content:str =  ""
    reasoning :str|None = None
    tool_call: dict|None = None
    metadata :dict |None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class LLM:

    model:str
    api_key:str  = "no_key"
    base_url:str = "http://localhost:11434/v1"
    think:bool = False

    def generate(self,messages:list[dict],tools:list|None = None) -> Response:

        body = {
            "model" : self.model,
            "messages" : messages,
        }
        if tools:
            body["tools"] = tools
        
        if not self.think:
            body["reasoning_effort"] = "none"

        
        request = urllib.request.Request(
            f"{self.base_url}/chat/completions",
            data = json.dumps(body).encode(),
            headers={
                "Content-Type" : "application/json",
                "Authorization" : f"Bearer {self.api_key}"
            }
           
        )

        with urllib.request.urlopen(request) as res:
            data = json.loads(res.read())

        message = data["choices"][0]["message"]
        tool_calls = message.get("tool_calls")
        tool_call = tool_calls[0] if tool_calls else None
        metadata = {
            "model":data["model"],
            "prompt_tokens":data["usage"]["prompt_tokens"],
            "completion_tokens":data["usage"]["completion_tokens"],
            
        }

        return Response(
            content=message["content"],
            reasoning=message.get("reasoning"),
            tool_call=tool_call,
            metadata=metadata
        )

        
            
            

        

    


        


    
    