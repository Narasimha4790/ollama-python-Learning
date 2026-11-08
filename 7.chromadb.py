import ollama
import chromadb

client=chromadb.Client()

texts = [
    "Python is a programming language.",
    "Ollama runs language models locally.",
    "RAG retrieves relevant information."
]

query = "What is RAG?"

embeds=[]
query_emb=[]

query_embeds=ollama.embeddings(
    model='nomic-embed-text',
    prompt=query
)

query_emb.append(query_embeds.embedding)



metadata=[{
    'source':'texts1',
    'page':1
    },
    {'source':'texts2',
    'page':2},
    {'source':'texts3',
        'page':3}]

for i in range(len(texts)):
    response=ollama.embeddings(
        model='nomic-embed-text',
        prompt=texts[i]
    )

    embeds.append(response.embedding)

collection=client.create_collection(name='python_docs')

collection.add(
    ids=['chunk1','chunk2','chunk3'],
    documents=texts,
    embeddings=embeds,
    metadatas=metadata
)

results=collection.query(
    query_embeddings=query_emb,
    n_results=1,
    include=['documents','metadatas','distances']
)

print(results['documents'])
print(results['metadatas'])
print(results['distances'])