### 1. Basic Chatbot (`1.chatbot.py`)

Created a basic command-line chatbot using Ollama
and the Llama 3.2 model.

**Concepts learned:**
- Integrating Ollama with Python.
- Interacting with a locally running LLM.
- Using the Ollama Chat API.
- Maintaining conversation history.
- Handling user input and model responses.

**Key learning:** Understanding how Python
communicates with a local language model and
maintains a conversation.


### 2. Text Embeddings (`2.embeds.py`)

Explored text embeddings using Ollama's
`nomic-embed-text` model.

**Concepts learned:**
- Understanding text embeddings.
- Generating embeddings using Ollama.
- Converting text into numerical vectors.
- Accessing and storing generated embeddings.

**Key learning:** Understanding how text is
represented as numerical vectors for further
processing in RAG applications.


### 3. Embedding Similarity (`3.embedding_similarity.py`)

Explored semantic similarity between sentences and
a query using text embeddings.

**Concepts learned:**
- Generating embeddings for multiple sentences.
- Generating query embeddings.
- Working with NumPy arrays.
- Reshaping arrays into 2D format.
- Understanding cosine similarity.
- Comparing sentence embeddings with query embeddings.

**Libraries used:**
- Ollama
- NumPy
- Scikit-learn

**Key learning:** Understanding how cosine similarity
helps identify how closely a sentence is related
to a given query.


### 4. PDF Text Extraction (`4.text_extraction.py`)

Implemented PDF text extraction using PyMuPDF.

**Concepts learned:**
- Opening PDF documents using PyMuPDF.
- Checking the number of pages.
- Loading individual pages.
- Extracting text using `get_text()`.
- Storing extracted text in a list.
- Combining extracted text into a single string.
- Handling `FileNotFoundError`.
- Closing PDF documents.

**Library used:**
- PyMuPDF

**Key learning:** Understanding how to extract
text from PDF documents using Python for further
processing in RAG applications.


### 5. Text Chunking (`5.chunking_practice.py`)

Explored different text chunking techniques as part
of the RAG learning process.

**Concepts learned:**
- Understanding text chunking.
- Word-based text splitting.
- Character-based text splitting.
- Configuring chunk size and overlap.
- Preserving context between consecutive chunks.
- Understanding separators in text splitting.

**Key learning:** Understanding how to divide large
documents into smaller, manageable chunks while
preserving context for better information retrieval.


### 6. Recursive Text Splitting (`6.recursive_textsplit.py`)

Explored recursive character-based text splitting
using LangChain.

**Concepts learned:**
- Understanding recursive text splitting.
- Using RecursiveCharacterTextSplitter.
- Configuring chunk size and chunk overlap.
- Understanding separators during text splitting.
- Preserving context between consecutive chunks.

**Library used:**
- langchain-text-splitters

**Key learning:** Understanding how recursive
splitting divides text into manageable chunks while
considering separators and preserving context.


### 7. Vector Database with ChromaDB (`7.chromadb.py`)

Implemented a basic vector database workflow using
ChromaDB and Ollama.

**Concepts learned:**
- Understanding vector databases.
- Creating a persistent ChromaDB client.
- Creating and retrieving collections.
- Generating document and query embeddings.
- Storing documents and embeddings in ChromaDB.
- Adding metadata to documents.
- Retrieving relevant documents using query embeddings.
- Understanding similarity distances.

**Libraries used:**
- Ollama
- ChromaDB

**Key learning:** Understanding how ChromaDB stores
and retrieves relevant information using vector
embeddings as part of a RAG application.