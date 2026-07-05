# 🤖 AI Business Proposal Generator

An autonomous AI-powered Business Proposal Generator built using **FastAPI**, **LangGraph**, **OpenAI GPT-4.1 Mini**, **Streamlit**, and **python-docx**.

The application accepts a natural language business request, automatically plans the work, generates a professional business proposal, exports it as a Microsoft Word document (`.docx`), and exposes the functionality through both a REST API and a Streamlit web interface.

---

# Features

- Autonomous AI Planning
- Business Proposal Generation
- LangGraph Workflow
- REST API using FastAPI
- Interactive Streamlit UI
- Microsoft Word (.docx) Export
- OpenAI GPT-4.1 Mini Integration
- Modular Project Architecture
- Professional Proposal Formatting

---

# Technology Stack

| Technology | Purpose |
|------------|---------|
| Python 3.12+ | Programming Language |
| FastAPI | REST API Backend |
| Streamlit | User Interface |
| LangGraph | AI Workflow Orchestration |
| OpenAI GPT-4.1 Mini | Proposal Generation |
| python-docx | Word Document Generation |
| Pydantic | Request & Response Validation |
| Uvicorn | ASGI Server |
| uv | Package Management |

---

# Project Structure

```text
AI-Business-Proposal-Generator/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   ├── openai_client.py
│   ├── planner.py
│   ├── planner_prompt.py
│   ├── proposal_prompt.py
│   ├── executor.py
│   ├── workflow.py
│   ├── doc_generator.py
│   ├── request.py
│   ├── response.py
│   ├── state.py
│   └── test.py
│
├── generated_docs/
│
├── streamlit_app.py
│
├── .env
├── .env.example
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Application Workflow

1. User submits a business request.
2. FastAPI receives the request.
3. LangGraph starts the workflow.
4. Planner analyzes the request.
5. Planner generates an execution plan.
6. Executor creates the business proposal.
7. Proposal is converted into a Word document.
8. API returns the generated proposal and document path.
9. Streamlit displays the output and allows downloading the document.

---

# AI Workflow

### Planner

The planner is responsible for:

- Understanding the user request
- Breaking the work into logical tasks
- Producing a structured execution plan

Example:

```text
1. Define business objectives
2. Identify the problem statement
3. Design the proposed solution
4. Prepare implementation timeline
5. Estimate budget assumptions
6. Describe expected benefits
7. Identify risks
8. Write conclusion
```

---

### Executor

The executor receives:

- Original User Request
- Planner Task List

It generates a complete professional business proposal using the LLM.

---

### Document Generator

The generated proposal is automatically converted into a Microsoft Word document.

Supported formatting:

- Headings
- Paragraphs
- Bullet Lists
- Numbered Lists

---

# REST API

## Health Check

### GET

```
/
```

Response

```json
{
    "status": "success",
    "message": "API is running."
}
```

---

## Generate Proposal

### POST

```
/agent
```

Request

```json
{
    "request":"Create a proposal for an AI Resume Screening System."
}
```

Example Response

```json
{
    "status":"success",
    "message":"Business proposal generated successfully.",
    "request":"Create a proposal for an AI Resume Screening System.",
    "tasks":[
        "...",
        "...",
        "..."
    ],
    "proposal":"...",
    "document":"generated_docs/proposal_xxxxxx.docx"
}
```

---

# Streamlit UI

The Streamlit interface provides:

- Business Request Input
- Example Prompts
- Workflow Status
- Generated Task List
- Proposal Preview
- Proposal Statistics
- Word Document Download
- Raw API Response

---

# Installation

Clone the repository

```bash
git clone <repository-url>

cd AI-Business-Proposal-Generator
```

Create Virtual Environment

```bash
uv venv
```

Activate Environment

Windows

```powershell
.venv\Scripts\Activate.ps1
```

Install Dependencies

```bash
uv pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file.

```env
OPENAI_API_KEY=your_openai_api_key
MISTRAL_API_KEY=your_mistral_api_key
```

---

# Running FastAPI

```bash
uvicorn app.main:app --reload
```

API

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

Redoc

```
http://127.0.0.1:8000/redoc
```

---

# Running Streamlit

```bash
streamlit run streamlit_app.py
```

Default URL

```
http://localhost:8501
```

---

# Output

Generated Word documents are stored inside

```text
generated_docs/
```

Example

```text
generated_docs/
    proposal_3dc9984b.docx
```

---

# Example Test Cases

### Test Case 1

```text
Create a proposal for an AI Resume Screening System.
```

---

### Test Case 2

```text
Create a proposal for an AI Hospital Management System.

Assume missing budget information.

Include implementation phases, risks, expected benefits, and a realistic timeline.
```

---

# Engineering Improvement

This project implements **Multi-Step Planning**.

Instead of generating a proposal directly, the AI first creates an execution plan.

Benefits:

- Better reasoning
- Structured execution
- Improved explainability
- Easier debugging
- Modular workflow

---

# Future Improvements

- Mistral AI Fallback
- Multi-Agent Workflow
- Proposal Templates
- Proposal History
- PDF Export
- Authentication
- Database Integration
- RAG for Company Templates
- Docker Deployment
- CI/CD Pipeline

---

# Author

**Aditya Singh**

---

# License

This project is created for an AI Engineering Assignment and is intended for educational and demonstration purposes.