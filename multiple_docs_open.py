import pymupdf
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb

path1="C://Users//91995//Downloads//Introduction to Python.pdf"
path2="C://Users//91995//Downloads//dummy.pdf"
documents=[]
final_chunk=[]
pdf_paths=[path1,path2]

for path in pdf_paths:
    doc=pymupdf.open(path)
    for page_num in range(doc.page_count):
        page=doc.load_page(page_num)
        text=page.get_text()
        documents.append({'text':text,'source':path,'page':page_num+1})

    doc.close()

print(documents)

splitter=RecursiveCharacterTextSplitter(
    chunk_size=30,
    chunk_overlap=10
)
for document in documents:
    text=document['text']
    chunks=splitter.split_text(text)
    for chunk in chunks:
        final_chunk.append({
            'text': chunk,
            'source': document['source'],
            'page': document['page']
        })

print(final_chunk)
