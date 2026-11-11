import ollama
import chromadb

client=chromadb.PersistentClient(path="./chroma_db")

texts = [
    "Python is a programming language.",
    "Ollama runs language models locally.",
    "RAG retrieves relevant information."
]

query = "What is RAG?"

embeds=[]
query_embed=[]

query_embeds=ollama.embeddings(
    model='nomic-embed-text',
    prompt=query
)

query_embed.append(query_embeds.embedding)

metadata=[{
    'source':'sentence1',
    'page':1
    },
    {'source':'sentence2',
    'page':1},
    {'source':'sentence3',
        'page':1}]

for i in range(len(texts)):
    response=ollama.embeddings(
        model='nomic-embed-text',
        prompt=texts[i]
    )

    embeds.append(response.embedding)

collection=client.get_or_create_collection(name='python_docs')

collection.add(
    ids=['chunk1','chunk2','chunk3'],
    documents=texts,
    embeddings=embeds,
    metadatas=metadata
)

results=collection.query(
    query_embeddings=query_embed,
    n_results=1,
    include=['documents','metadatas','distances'],
    where={'source':'sentence3'}
)

print(results['documents'])
print(results['metadatas'])
print(results['distances'])