import ollama


embeds_=ollama.embeddings(
    model='nomic-embed-text',
    prompt='what is python. i love programming. i enjoy writing code'
)

vector=embeds_.embedding

print(vector)

#print(len(vector))--Answer is 768