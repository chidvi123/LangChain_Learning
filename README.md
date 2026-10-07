# Week 5 — LangChain, RAG & Vector Search

A hands-on learning project focused on **LangChain, embeddings, vector databases, retrieval, RAG, reranking, and RAG evaluation**.

The goal of this repository is not just to learn how to build a RAG application, but to understand **what happens behind the scenes at every stage of the retrieval pipeline** and how these concepts are used in production systems.

---

## 🎯 Objectives

By the end of this project, I aim to understand:

- How LangChain works as an orchestration framework
- How different LLM providers are integrated with LangChain
- How documents are loaded and processed
- Why documents need to be chunked
- How different chunking strategies work
- What embeddings are and how they are generated
- How embedding dimensions affect storage and retrieval
- How vector databases store and retrieve vectors
- How similarity search works
- How retrieval works internally
- How reranking improves retrieval quality
- Latency and throughput considerations
- How a complete RAG pipeline works
- How to evaluate RAG systems
- What LangChain abstracts compared with implementing the retrieval pipeline manually

---

# 🧠 Topics Covered

## 1. LangChain Ecosystem

Understanding the LangChain ecosystem and its different packages/integrations.

### Topics

- `langchain-core`
- `langchain-community`
- `langchain-text-splitters`
- `langchain-groq`
- `langchain-openai`
- `langchain-anthropic`
- LLM provider integrations
- Abstraction and orchestration
- LangChain components and interfaces

### Key Idea

LangChain provides a common framework for composing different components and integrating with different LLM providers and external technologies.

---

## 2. Prompt Templates

- `PromptTemplate`
- `ChatPromptTemplate`
- System / Human / AI messages
- Dynamic prompt variables
- Reusable prompts

---

## 3. LCEL — LangChain Expression Language

- Runnables
- Pipe operator `|`
- Composing components
- Chain construction
- `.invoke()`
- `.stream()`
- Data flow between components

Example:

```python
chain = prompt | llm | parser
```

---

## 4. Output Parsers

- `StrOutputParser`
- `CommaSeparatedListOutputParser`
- `JsonOutputParser`
- `PydanticOutputParser`
- Structured outputs
- Output validation

---

## 5. Document Loaders

Loading different types of external data into LangChain `Document` objects.

### Sources

- TXT
- PDF
- CSV
- DOCX
- Markdown
- JSON
- Web data

### Core concepts

```text
Source Document
      ↓
Document Loader
      ↓
LangChain Document
      ↓
page_content + metadata
```

---

# 6. Chunking / Text Splitting

Understanding why and how documents are divided into smaller pieces before embedding.

### Topics

- Why chunking is required
- Chunk size
- Chunk overlap
- Recursive character splitting
- Character-based chunking
- Sentence-based chunking
- Token-based chunking
- Semantic chunking
- Markdown / HTML-aware chunking
- Code-aware chunking
- Parent-child chunking
- Contextual chunking
- Metadata preservation
- Chunking strategies for different data types

### Data types

- PDF
- DOCX
- TXT
- CSV
- Markdown
- JSON
- Source code

---

# 7. Embeddings

Understanding how text is converted into numerical vector representations.

### Topics

- What are embeddings?
- Why embeddings are required
- How embedding models work
- Text → vector transformation
- Dense embeddings
- Sparse embeddings
- Static embeddings
- Contextual embeddings
- Query embeddings
- Document embeddings
- Embedding dimensions
- Vector normalization
- Embedding storage
- Memory requirements
- Embedding latency and cost

Example:

```text
Text
 ↓
Embedding Model
 ↓
[0.12, -0.43, 0.87, ...]
```

---

# 8. Vector Stores & Vector Databases

Understanding how embeddings are stored and searched.

### Topics

- What is a vector store?
- What is a vector database?
- Vector store vs vector database
- Normal database vs vector database
- Vector storage
- Metadata storage
- Indexing
- Exact nearest-neighbor search
- Approximate nearest-neighbor (ANN) search
- HNSW
- IVF
- Product Quantization
- Filtering
- Memory vs disk
- Scaling
- Sharding
- Replication
- Large-scale enterprise vector storage

---

# 9. Similarity Search

Understanding how vectors are compared to determine semantic similarity.

### Similarity / distance methods

- Cosine similarity
- Dot product
- Euclidean distance
- Manhattan distance
- Similarity vs distance
- Vector normalization
- Top-k search
- Similarity thresholds

Basic flow:

```text
User Query
    ↓
Query Embedding
    ↓
Similarity Search
    ↓
Ranked Results
    ↓
Top-k Chunks
```

---

# 10. Retrieval

Understanding how relevant information is retrieved from a knowledge base.

### Topics

- Dense retrieval
- Sparse retrieval
- Hybrid retrieval
- Metadata filtering
- Top-k retrieval
- Similarity thresholds
- Query expansion
- Multi-query retrieval
- Parent-document retrieval
- Context compression

---

# 11. Reranking

Improving the relevance of retrieved documents before sending them to the LLM.

### Topics

- Why reranking is needed
- Retriever vs reranker
- Candidate retrieval
- Bi-encoder
- Cross-encoder
- Reranking pipeline
- Accuracy vs latency trade-offs

Example:

```text
Query
 ↓
Vector Search
 ↓
Top 20 Candidates
 ↓
Reranker
 ↓
Top 5 Relevant Chunks
 ↓
LLM
```

---

# 12. Latency & Throughput

Understanding performance characteristics of retrieval systems.

### Topics

- Request latency
- Embedding latency
- Vector search latency
- Reranking latency
- LLM latency
- End-to-end latency
- Throughput
- Concurrent requests
- Batching
- Caching
- Scalability
- Performance trade-offs

---

# 13. RAG — Retrieval-Augmented Generation

Understanding the complete RAG architecture.

## Ingestion Pipeline

```text
Documents
    ↓
Document Loader
    ↓
Chunking
    ↓
Embedding Model
    ↓
Vector Database
    ↓
Vector Index
```

## Query Pipeline

```text
User Question
      ↓
Query Embedding
      ↓
Vector Search
      ↓
Top-k Candidates
      ↓
Reranking
      ↓
Relevant Context
      ↓
Prompt
      ↓
LLM
      ↓
Answer
```

---

# 14. RAG Evaluation

Measuring the quality of retrieval and generated answers.

### Topics

- Retrieval evaluation
- Generation evaluation
- Precision
- Recall
- Recall@k
- Hit@k
- Mean Reciprocal Rank (MRR)
- Context relevance
- Answer relevance
- Faithfulness
- Groundedness
- LLM-as-a-Judge
- Test datasets
- Evaluation experiments

---

# 🛠️ Hands-on Approach

This project will use **two implementation approaches**.

## 1. Under-the-Hood Implementation

Implement the important retrieval concepts manually using Python and supporting libraries.

The purpose is to understand what happens internally.

```text
Documents
   ↓
Chunking
   ↓
Embeddings
   ↓
Vectors
   ↓
Similarity Calculation
   ↓
Top-k Retrieval
   ↓
Context
   ↓
LLM
```

This helps understand what frameworks and vector databases are actually doing behind the scenes.

---

## 2. LangChain Implementation

Build the same concepts using LangChain.

```text
Document Loader
      ↓
Text Splitter
      ↓
Embeddings
      ↓
Vector Store
      ↓
Retriever
      ↓
Reranker
      ↓
Prompt
      ↓
LLM
      ↓
Output Parser
      ↓
Answer
```

The goal is to understand **what LangChain abstracts for us**.

---

# 🚀 Final Project

Build a complete document-based RAG application using:

- Document loaders
- Chunking
- Embeddings
- Vector database
- Similarity search
- Retrieval
- Reranking
- LLM
- LangChain
- RAG evaluation

The system should be able to:

1. Ingest documents
2. Split documents into appropriate chunks
3. Generate embeddings
4. Store vectors and metadata
5. Accept user questions
6. Generate query embeddings
7. Retrieve relevant chunks
8. Rerank retrieved results
9. Generate grounded answers
10. Evaluate retrieval and answer quality

---

# 📁 Project Structure

The structure will evolve as the project progresses.

```text
Week5_LangChain/
│
├── 01_prompt_templates/
│
├── 02_lcel/
│
├── 03_output_parsers/
│
├── 04_document_loaders/
│
├── 05_text_splitters/
│
├── 06_embeddings/
│
├── 07_vector_stores/
│
├── 08_similarity_search/
│
├── 09_retrieval/
│
├── 10_reranking/
│
├── 11_rag/
│
├── 12_rag_evaluation/
│
├── final_project/
│
├── .env
├── .gitignore
└── README.md
```

---

# 🔐 Environment Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

API keys should be stored in `.env` and **never committed to GitHub**.

Example:

```env
GROQ_API_KEY=your_api_key_here
```

`.gitignore` should contain:

```text
.venv/
.env
__pycache__/
```

---

# 🎯 Learning Philosophy

This project focuses on **understanding rather than memorization**.

I don't need to memorize every LangChain package, vector database, embedding model, or integration.

Instead, I aim to understand:

> **What it is → Why it is needed → How it works → What happens internally → What alternatives exist → What trade-offs exist → How to implement it.**

---

# 📌 Current Progress

- [x] LangChain fundamentals
- [x] Prompt Templates
- [x] Chat Prompt Templates
- [x] LCEL
- [x] Chains
- [x] Output Parsers
- [x] Document Loaders
- [ ] Chunking / Text Splitting
- [ ] Embeddings
- [ ] Vector Stores / Vector Databases
- [ ] Similarity Search
- [ ] Retrieval
- [ ] Reranking
- [ ] Latency & Throughput
- [ ] RAG Architecture
- [ ] RAG Evaluation
- [ ] Final RAG Hands-on Project

---

# 📚 Goal

The final goal is to be able to explain and implement a complete RAG system from first principles, while also understanding how frameworks such as **LangChain abstract and orchestrate the underlying components**.