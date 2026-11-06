text = "Python is easy. Ollama runs local models. RAG retrieves information. Embeddings convert text into vectors."

words=text.split(" ")

chunk_size=4
overlap=1

print("\n\n")

list_=[]
chunks=[]

for word in words:
  list_.append(word)
  if len(list_) == chunk_size:
    chunks.append(list_)
    list_=list_[-overlap:]  # overlap
if list_:
    chunks.append(list_)

for chunk in chunks:
  print(chunk)