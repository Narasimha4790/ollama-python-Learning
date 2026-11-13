import ollama
import chromadb

query="what python is used for?"

query_embeds=ollama.embeddings(
    model='nomic-embed-text',
    prompt=query
)

client=chromadb.PersistentClient(path="./chroma_db")

collection=client.get_collection(name='python_docs')

result=collection.query(
    query_embeddings=[query_embeds.embedding],
    n_results=3
)

context=" ".join(result['documents'][0])

prompt=f"""Stay grounded to the providing document and generate an accurate answer for the given query. context={context}, query={query}"""
answer=ollama.generate(
model='llama3.2',
prompt=prompt
)

print(answer.response)