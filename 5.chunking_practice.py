text = "Python is easy. Ollama runs local models. RAG retrieves information. Embeddings convert text into vectors."

words=text.split(" ")
print(words)

print("\n\n")
list_=[]
chunks=[]

for word in words:
  list_.append(word)
  if len(list_) == 4:
    chunks.append(list_)
    list_=[]
if list_:
    chunks.append(list_)

for chunk in chunks:
  print(chunk)