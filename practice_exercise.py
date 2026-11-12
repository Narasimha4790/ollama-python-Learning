import pymupdf
from langchain_text_splitters import RecursiveCharacterTextSplitter

# adding file
path="c://Users//91995//Downloads//Introduction to Python.pdf"

document=pymupdf.open(path)

page=document.load_page(0)
text=page.get_text()

# splitting and generating chunks

splitter=RecursiveCharacterTextSplitter(
    chunk_size=25,
    chunk_overlap=10
)

chunks=splitter.split_text(text)

print(chunks)