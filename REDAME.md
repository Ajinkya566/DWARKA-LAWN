# METRO Sales Assistant – Agentic AI Demo

## 1. Project Overview
This project is a local Agentic AI Sales Assistant that answers questions about sales data and Sales SOP documents using natural language.

## 2. Problem Statement
Business users need a simple way to retrieve sales insights and policy information without manually searching CSV files and SOP documents.

## 3. Technologies Used
- Python
- Streamlit
- LangGraph
- LangChain
- Ollama (Llama 3.2)
- FAISS Vector Store
- RAG (Retrieval-Augmented Generation)
- Pandas
- Pytest
- Python Logging

## 4. Architecture
1. User enters a question through the Streamlit UI.
2. LangGraph agent analyses the question.
3. Sales-related questions use Python tools to retrieve data from CSV.
4. SOP-related questions use RAG to retrieve relevant document chunks.
5. FAISS performs similarity search using embeddings.
6. Ollama generates the final response.
7. Streamlit displays the answer.
8. Logging records request status and errors.

## 5. Project Structure
- `app.py` – Streamlit user interface and chat history
- `agent.py` – Agent setup and tool orchestration
- `tools.py` – Sales data tools
- `rag.py` – Document retrieval using RAG and FAISS
- `data/sales_data.csv` – Sample sales dataset
- `data/sales_sop.txt` – Sample SOP document
- `tests/` – Automated tests
- `app.log` – Application logs

## 6. Setup Instructions
Install the required packages:

```bash
pip install streamlit langchain langgraph langchain-openai pandas python-dotenv langchain-ollama faiss-cpu
```

Ensure Ollama is installed and the required models are available:

```bash
ollama pull llama3.2:3b
ollama pull nomic-embed-text
```

Activate the project's virtual environment if applicable.

## 7. Run the Application

```bash
streamlit run app.py
```

Open the local URL shown in the terminal.

## 8. Sample Questions
- What is the total sales?
- Which product has the lowest sales?
- Which product has the highest sales?
- What is the sales return policy?

## 9. Testing
Automated tests are maintained in the `tests/` directory.

Run tests using:

```bash
python -m pytest -v
```

## 10. Logging
The application records successful agent requests and errors in `app.log`. Logs help troubleshoot application failures.

## 11. Future Improvements
- Add authentication and role-based access
- Improve retrieval relevance and source citations
- Add response evaluation and monitoring
- Deploy the application to a cloud environment
- Add production-grade error handling and observability

## 12. Important Note
This is a demonstration project using synthetic sample data. It is not an official METRO production system.