from memory import Memory
from embedding import EmbeddingModel



class RAGMemory(Memory):

    def __init__(self,embedding_model:EmbeddingModel,documents: list[str],top_k:int = 3):
        super().__init__()
        self.embedding_model = embedding_model
        self.docs = documents
        self.embeddings = [embedding_model.embed(doc) for doc in documents]
        self.top_k = top_k
    

    def _cosine(self, a:list[float],b:list[float]) -> float:
        return sum(x*y for x,y in zip(a,b)) / (sum(x*x for x in a)**0.5 * sum(y*y for y in b)**0.5)

    
    def search(self,query:str) -> list[str]:

        query_emb = self.embedding_model.embed(query)
        scores = [(doc,self._cosine(query_emb,doc_emb)) for doc,doc_emb in zip(self.docs,self.embeddings)]
        scores.sort(key=lambda x: x[1],reverse=True)
        return [doc for doc,score in scores[:self.top_k]]


    

    def add(self,role:str,content:str,**kwargs) -> None:

        if role == "user":
            context = "\n".join(self.search(content))
            content = f"""Context:
                        {context}
                        Question: {content}"""
        
        super().add(role,content,**kwargs)
        
        