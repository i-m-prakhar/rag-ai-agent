# RAG AI Agent

A Python-based **Retrieval-Augmented Generation (RAG)** application that enables users to upload PDF documents and ask questions about their content using AI. The system combines semantic search with large language models (LLMs) to generate contextually relevant answers grounded in the uploaded documents.

This project focuses on production-oriented AI engineering practices, including workflow orchestration, observability, retries, rate limiting, and concurrency control.

## Key Features

- **PDF Ingestion:** Load and process PDF documents for retrieval.
- **Text Chunking & Embeddings:** Split documents into smaller chunks and convert them into vector embeddings.
- **Semantic Search:** Retrieve relevant document content using vector similarity search.
- **AI-Powered Q&A:** Generate context-aware answers using retrieved information and an LLM.
- **Workflow Orchestration:** Manage asynchronous tasks and background workflows.
- **Reliability & Observability:** Incorporate error handling, retries, monitoring, rate limiting, and concurrency controls.
- **Interactive UI:** Provide a simple interface for document queries.

## Architecture

The application follows a modular RAG pipeline:

1. **Ingestion:** Load PDF documents and split their content into manageable chunks.
2. **Embedding & Storage:** Generate embeddings and store them in a vector database.
3. **Retrieval:** Convert user queries into embeddings and retrieve relevant document chunks.
4. **Generation:** Pass the retrieved context to an LLM to generate relevant responses.
5. **Orchestration:** Coordinate workflows and improve reliability through retries, monitoring, and execution controls.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| FastAPI | Backend API |
| OpenAI | Embeddings and LLM-powered responses |
| Qdrant | Vector database and semantic search |
| LlamaIndex | Document loading and processing |
| Inngest | Workflow orchestration |
| Streamlit | Interactive frontend |
| uv | Python dependency and project management |

## Getting Started

### Prerequisites

- Python
- uv
- Docker
- OpenAI API key

### Installation

Clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd <project-directory>
```

Install dependencies:

```bash
uv sync
```

Configure the required environment variables in a `.env` file, including your OpenAI API key and any other settings required by the application.

Start the required services and run the backend, workflow development server, and frontend using the commands configured in the project.

> **Note:** Refer to the project configuration and application entry points for the exact commands required to run each service.

## Learning Objectives

- Building Retrieval-Augmented Generation (RAG) pipelines
- Working with vector databases and semantic retrieval
- Developing LLM-powered applications in Python
- Implementing asynchronous workflows and background processing
- Applying reliability and observability practices to AI applications

  
---

*An AI engineering project exploring practical RAG implementation and production-oriented application architecture.*
