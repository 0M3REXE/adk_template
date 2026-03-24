<div align="center">

# 🤖 ADK Agent Template

**A production-ready starter template for building intelligent multi-agent systems with [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/)**

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python)](https://www.python.org/)
[![Google ADK](https://img.shields.io/badge/Google%20ADK-1.2%2B-orange?logo=google)](https://google.github.io/adk-docs/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104%2B-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![uv](https://img.shields.io/badge/uv-package%20manager-5C3EE8)](https://docs.astral.sh/uv/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 📖 Overview

This repository is a **professional, batteries-included template** for rapidly spinning up AI agents powered by Google's Agent Development Kit (ADK). It ships with a fully functional **Python Teacher** multi-agent system as a reference implementation, demonstrating real-world patterns such as:

- Orchestrating **multiple specialised sub-agents** from a single root agent
- Integrating **Google Search** and a **built-in code executor** as agent tools
- Serving the agent over HTTP via a **FastAPI** web interface
- Managing conversations with a **persistent SQLite session store**

Use this template as your launchpad — swap out the Python Teacher logic for your own domain, add tools, and deploy with confidence.

---

## 🌟 Why Templates Matter

Starting an AI agent project from scratch involves a surprising amount of boilerplate: choosing a package manager, wiring up a web server, configuring CORS, managing sessions, registering modules correctly, and structuring your code so the ADK framework can discover your agents. Getting even one of these details wrong can cost hours of debugging.

A well-crafted template eliminates that friction:

| Without a template | With this template |
|---|---|
| Hours spent on project scaffolding | **< 5 minutes** to a running agent |
| Trial-and-error framework configuration | Pre-configured, battle-tested setup |
| Copy-pasting boilerplate across projects | Clean, reusable starting point |
| Inconsistent project structure across a team | Standardised layout everyone understands |
| Potential misconfigurations in production | Best-practice defaults already in place |

Templates also serve as **living documentation** — the code itself teaches you how the pieces fit together, making onboarding new contributors fast and painless.

---

## ✨ Features

- ⚡ **Blazing-fast setup** with [`uv`](https://docs.astral.sh/uv/) — the modern Python package manager
- 🧠 **Multi-agent architecture** — a root orchestrator delegates to specialised sub-agents
- 🔍 **Google Search integration** — real-time web search inside your agent
- 💻 **Built-in code executor** — execute Python code sandboxed within the agent
- 🌐 **FastAPI web server** — production-ready HTTP API with auto-generated docs
- 💾 **Persistent sessions** — SQLite-backed conversation history out of the box
- 🔧 **Minimal, readable codebase** — easy to extend and customise

---

## 🏗️ Project Structure

```
adk_template/
├── agent/
│   ├── __init__.py        # Exports the agent module
│   └── agent.py           # Agent definitions (root + sub-agents)
├── main.py                # FastAPI application entry point
├── pyproject.toml         # Project metadata and dependencies
├── uv.lock                # Locked dependency tree
├── .python-version        # Pinned Python version
├── sessions.db            # SQLite session storage (auto-created)
└── README.md
```

---

## 🤖 Agent Architecture

```
root_agent  (Python_Teacher — gemini-2.0-flash)
├── SearchAgent             Google Search specialist
│   └── tool: google_search
└── CodeAgent               Python code execution specialist
    └── tool: BuiltInCodeExecutor
```

The **root agent** classifies every incoming message and routes it to the right specialist:

| Input type | Handler |
|---|---|
| General Python question | Root agent answers directly |
| Code problem / demonstration | Delegated to **CodeAgent** |
| Web lookup / latest docs | Delegated to **SearchAgent** |
| Mathematical calculation | Delegated to **CodeAgent** |

---

## 🚀 Quick Start

### Prerequisites

- Python **3.12+**
- [`uv`](https://docs.astral.sh/uv/getting-started/installation/) installed globally
- A **Google API key** with Gemini access ([get one here](https://aistudio.google.com/app/apikey))

### 1 — Clone and enter the project

```bash
# Replace the URL below with your own fork if you are using this as a template
git clone https://github.com/0M3REXE/adk_template.git
cd adk_template
```

### 2 — Create and activate a virtual environment

```bash
uv venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3 — Install dependencies

```bash
uv sync
```

### 4 — Configure environment variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

### 5 — Run the agent

**Option A — ADK built-in web UI (recommended for development)**

```bash
adk web
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

**Option B — FastAPI server**

```bash
python main.py
```

The API will be available at [http://localhost:8080](http://localhost:8080).  
Interactive API docs: [http://localhost:8080/docs](http://localhost:8080/docs)

---

## 🛠️ Building Your Own Agent

This template is intentionally simple so it is easy to adapt. Here is a typical workflow:

1. **Rename** `agent/` to your own module name (e.g. `customer_support/`).
2. **Edit** `agent/agent.py` — change `APP_NAME`, `MODEL`, and the agent instructions.
3. **Add tools** — import any ADK-compatible tool and pass it in the `tools=[...]` list.
4. **Update** `main.py` if you renamed the module.
5. **Deploy** — the FastAPI app is ready to containerise or deploy to Cloud Run.

### Creating a new project from scratch with `uv`

```bash
# Initialise a new project
uv init my-adk-agent
cd my-adk-agent

# Add Google ADK and optional extras
uv add google-adk
uv add langchain-community tavily-python litellm   # optional

# Sync the environment
uv sync
```

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `google-adk` | Agent Development Kit core framework |
| `fastapi` | High-performance web framework |
| `uvicorn` | ASGI server for FastAPI |
| `pydantic` | Data validation and settings management |
| `python-multipart` | Multipart form data support |

---

## 🤝 Contributing

Contributions, bug reports and feature requests are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "feat: add my feature"`
4. Push and open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ using [Google ADK](https://google.github.io/adk-docs/)

</div>
