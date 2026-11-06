import ollama
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

sentences=["I love programming.","Cricket is a popular sport.","Python is used for machine learning."]

vector=[]
query_vector=[]
query="How is Python used?"

for i in range(len(sentences)):

    embed_=ollama.embeddings(
        model='nomic-embed-text',
        prompt=sentences[i]
    )
    vector.append(embed_.embedding)

query_embed=ollama.embeddings(
    model='nomic-embed-text',
    prompt=query
)
query_vector.append(query_embed.embedding)

p=vector[0]
q=vector[1]
r=vector[2]

arr1=np.array(p)
arr2=np.array(q)
arr3=np.array(r)

query_array=np.array(query_vector)

matrix1=arr1.reshape(1,-1)
matrix2=arr2.reshape(1,-1)
matrix3=arr3.reshape(1,-1)

query_matrix=query_array.reshape(1,-1)

cs1=cosine_similarity(matrix1,query_matrix)
cs2=cosine_similarity(matrix2,query_matrix)
cs3=cosine_similarity(matrix3,query_matrix)

print("First sentence similarity with query",cs1)
print("Second sentence similarity with query",cs2)
print("Third sentence similarity with query",cs3)

