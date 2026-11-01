# NexusAI-Multi-Agent-Platform
An autonomous multi-agent AI platform powered by LangGraph, Groq, and Tavily that can research, generate code, review solutions, and create intelligent reports.

# NexusAI | Multi-Agent-Platform 🤖

### Autonomous Multi-Agent Intelligence & Execution Platform

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://python.org/)
[![Flask](https://img.shields.io/badge/Flask-Backend-black?logo=flask)](https://flask.palletsprojects.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Orchestration-1C3C3C)](https://www.langchain.com/langgraph)
[![Groq](https://img.shields.io/badge/Groq-LLM-orange)](https://groq.com/)
[![Tavily](https://img.shields.io/badge/Tavily-Web_Search-blue)](https://tavily.com/)

[![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker&logoColor=white)](https://docker.com/)
[![Gunicorn](https://img.shields.io/badge/Gunicorn-Production_Server-499848)](https://gunicorn.org/)
[![Deployment](https://img.shields.io/badge/Deployment-Render-46E3B7?logo=render&logoColor=black)](https://render.com/)

</div>

---

## 🚀 Overview

**NexusAI** is an autonomous multi-agent AI platform designed to handle research, code generation, code review, and intelligent report creation.

Built with **Python, Flask, LangGraph, Groq, and Tavily**, it coordinates specialized AI agents through structured workflows to transform user instructions into meaningful results.

<img width="1351" height="638" alt="image" src="https://github.com/user-attachments/assets/ef102e01-31e5-4f1e-bfe3-e051f36f5e40" />


## ✨ Key Features

- 🧠 **Manager Agent:** Understands and classifies user tasks.
- 🔍 **Research Agent:** Performs web research using Tavily.
- 💻 **Coding Agent:** Generates code based on user requirements.
- 🧪 **Testing Agent:** Reviews generated code and identifies potential issues.
- 📊 **Report Agent:** Creates structured final reports.
- 🔗 **LangGraph Workflow:** Coordinates multiple agents intelligently.
- ⚡ **Groq Integration:** Provides LLM-powered responses.
- 🌐 **Interactive Dashboard:** User-friendly web interface.
- 🐳 **Docker Support:** Containerized application deployment.

## 🏗️ System Architecture

```text
              USER INPUT
                  |
                  v
             MANAGER AGENT
                  |
          TASK CLASSIFICATION
                  |
        +---------+---------+
        |         |         |
        v         v         v
     RESEARCH   CODING   GENERAL
      AGENT      AGENT     TASK
        |         |
        |         v
        |      TESTING
        |       AGENT
        |         |
        +----+----+
             |
             v
         REPORT AGENT
             |
             v
        FINAL RESPONSE
```

### Agent Workflow

| Task Type | Execution Flow |
|---|---|
| Research | Manager → Research → Report |
| Coding | Manager → Coding → Testing → Report |
| General | Manager → Report |

> **Note:** The Testing Agent currently performs code review; automatic code execution is a planned enhancement.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Backend development |
| Flask | Web framework |
| HTML, CSS, JavaScript | Frontend |
| LangGraph | Agent orchestration |
| LangChain | AI integration |
| Groq | LLM inference |
| Tavily | Web search |
| Docker | Containerization |
| Gunicorn | Production server |

## 📁 Project Structure

```text
NexusAI-Multi-Agent-Platform/
│
├── app.py
├── agents.py
├── graph.py
├── tools.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── .env
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/prajapatishubham336/NexusAI-Multi-Agent-Platform.git
cd NexusAI-Multi-Agent-Platform
```

**2. Create and activate virtual environment**

```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure environment variables**

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
GROQ_MODEL=openai/gpt-oss-120b
```

API keys:
- [Groq Console](https://console.groq.com/keys)
- [Tavily](https://app.tavily.com/)

**5. Start the application**

```bash
python app.py
```

Open: `http://127.0.0.1:5000`

## 🐳 Docker Setup

Build the Docker image:

```bash
docker build -t nexusai .
```

Run the container:

```bash
docker run --name nexusai-test --env-file .env -p 10000:10000 nexusai
```

Open: `http://localhost:10000`

## ☁️ Deployment

NexusAI supports Docker-based deployment.

Deployment workflow:
1. Push the project to GitHub.
2. Connect the repository to Render.
3. Create a Docker Web Service.
4. Configure `GROQ_API_KEY`, `TAVILY_API_KEY`, and `GROQ_MODEL`.
5. Deploy and access the public application URL.

**Security:** Never commit `.env` or expose API keys in your public repository.

## 🔮 Future Enhancements

- Automated code execution with secure sandboxing.
- Persistent AI memory and chat history.
- User authentication and personalized workspaces.
- Real-time agent execution monitoring.
- File upload and document analysis.
- Additional specialized AI agents.

## 👨‍💻 Author

**Shubham Prajapati**

AI / ML Engineer | Generative AI | Machine Learning

GitHub: [@prajapatishubham336](https://github.com/prajapatishubham336)

---

<div align="center">

### NexusAI

**Think Smarter. Research Faster. Execute Better.**

⭐ If you like this project, consider giving it a star!

**Built with ❤️ by Shubham Prajapati**

</div>
