# 🧠 Agentic Knowledge Base Platform

A modular, scalable, and agentic AI-powered knowledge base platform built with LangGraph, CrewAI, AutoGen, and Gemini API. Designed for both guest and authenticated users, with support for file uploads, RAG, and multi-agent orchestration.

---

## 🚀 Features

- 🔐 Guest & Authenticated User Modes
- 📁 File Uploads (PDF, DOCX, TXT)
- 🧠 RAG with FAISS/Chroma + PostgreSQL
- 🤖 Agentic AI Workflows (LangGraph, CrewAI, AutoGen)
- 🌐 Admin-curated Global Knowledge Base
- 🧩 Modular Backend (Python + .NET Core)
- 🖥️ Gradio UI (React/Blazor-ready)
- 🐳 Dockerized for local and cloud deployment

---

## 🧱 Architecture Overview
Frontend (Gradio/React) ↓ API Layer (FastAPI / .NET Core) ↓ ├── Non-Agentic Backend (Auth, KB, File, DB) └── Agentic AI Backend (LangGraph, CrewAI, AutoGen, Gemini) ↓ PostgreSQL + FAISS/Chroma + Redis


---

## 🗂️ Folder Structure
agentic-kb-platform/ ├── backend/         # Auth, KB, File, Vector services ├── agents/          # Agent registry, workflows, tools ├── api/             # FastAPI entry point and routes ├── database/        # Schema, migrations, ORM models ├── frontend/        # Gradio UI and future React UI ├── docker/          # Dockerfiles and Compose setup ├── scripts/         # Seeders, test runners, utilities ├── tests/           # Unit and integration tests └── .env/            # Environment config


---

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| **Frontend** | Gradio, React (future) |
| **Backend** | FastAPI, .NET Core |
| **Agents** | LangGraph, CrewAI, AutoGen, Gemini API |
| **Database** | PostgreSQL, FAISS/Chroma, Redis |
| **DevOps** | Docker, DBeaver, Postman |

---

## 🧪 Getting Started

```bash
# Clone the repo
git clone https://github.com/your-username/agentic-kb-platform.git
cd agentic-kb-platform

# Set up environment
cp .env/dev.env .env

# Start services
docker-compose up --build

📌 Roadmap
- [x] PostgreSQL schema + seeders
- [x] Guest user flow with public KB
- [ ] Agent registry + LangGraph workflows
- [ ] React UI with chat + file upload
- [ ] Cloud DB migration support

👤 Author
Gunjan Tailor
Senior Consultant – Backend, Automation & Agentic AI

📄 License
MIT License

---

Let me know if you want me to generate:
- GitHub issue labels (e.g., `agent`, `backend`, `frontend`, `infra`)
- A `CONTRIBUTING.md` or `docker-compose.yml`
- A visual architecture diagram to embed in the README

You're building something powerful—this is going to be a standout project.
