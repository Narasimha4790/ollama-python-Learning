import pymupdf
import ollama
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb

# adding file
try:
    path="c://Users//91995//Downloads//Introduction to Python.pdf"
    document=pymupdf.open(path)

except FileNotFoundError:
    print("Enter valid path")
else:

    page=document.load_page(0)
    text=page.get_text()
    document.close()

# splitting and generating chunks

splitter=RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=10
)

chunks=splitter.split_text(text)

# Generating Embeddings
embeds=[]

for chunk in chunks:
    response=ollama.embeddings(
        model='nomic-embed-text',
        prompt=chunk
    )
    embeds.append(response.embedding)


client=chromadb.Client()

collection=client.create_collection(name='practice')

id=[]
final_md=[]
for i in range(len(embeds)):
    id.append(str(i))
    final_md.append({"source": "document1",
        "page": 1})

collection.add(
    ids=id,
    metadatas=final_md,
    embeddings=embeds,
    documents=chunks
)

query = "Where python is used?"
query_embed=[]

query_embeds=ollama.embeddings(
    model='nomic-embed-text',
    prompt=query
)

query_embed.append(query_embeds.embedding)

results=collection.query(
    query_embeddings=query_embed,
    n_results=3,
    include=['documents','metadatas']
)

context=results['documents'][0][0]
prompt=f"""Answer strictly using the provided context. 
If the answer is not available in the context, say Information not found in the document. 

context={context} 
question={query}"""

answer=ollama.generate(
model='llama3.2',
prompt=prompt
)

print(answer.response)