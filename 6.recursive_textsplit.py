from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """Python is easy to learn.
Ollama runs local models.
RAG retrieves relevant information."""

splitter=RecursiveCharacterTextSplitter(
    chunk_size=25,
    chunk_overlap=10,
)

chunks=splitter.split_text(text)

print(chunks)