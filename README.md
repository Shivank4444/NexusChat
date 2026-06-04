# NexusChat 🤖

An Agentic AI-powered chatbot application built using LangGraph, LangChain, Streamlit, Groq LLM interface and Tavily Search. The project demonstrates intelligent conversational workflows, web search integration, and AI news summarization through a graph-based architecture.

---

## 🚀 Features

- 💬 Basic AI Chatbot using Groq LLM interface
- 🌐 Web-Enabled Chatbot with Search Tool Integration
- 📰 AI News Summarization (Daily, Weekly, Monthly, Yearly)
- 🔄 LangGraph-based Agent Workflow Management
- 🎨 Interactive Streamlit User Interface
- ⚡ Fast LLM Inference using Groq
- 🔍 Real-time Web Search with Tavily API

---

## 🛠️ Tech Stack

### Frameworks & Libraries
- LangGraph
- LangChain
- Streamlit
- Groq API
- Tavily Search API

### Programming Language
- Python 3.11+


---

## 📂 Project Structure

```bash
NexusChat/
│
├── AINews/
│
├── src/
│   └── langgraphagenticai/
│       │
│       ├── graph/          # LangGraph workflow definitions
│       ├── LLMS/           # LLM configuration and initialization
│       ├── nodes/          # Agent and workflow nodes
│       ├── state/          # Shared state management
│       ├── tools/          # External tools and integrations
│       ├── ui/
│       │   └── streamlitui/
│       │       ├── display_result.py
│       │       ├── loadui.py
│       │       └── uiconfigfile.py
│       │
│       ├── main.py
│       └── __init__.py
│
├── app.py                  # Application entry point
├── requirements.txt
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Shivank4444/NexusChat.git
cd NexusChat
```

### 2. Create Virtual Environment

```bash
uv venv
```

### 3. Install Dependencies

```bash
uv sync
```

---

## 🔑 API Keys Required

### Groq API Key

Create an account at:

https://console.groq.com

### Tavily API Key

Create an account at:

https://tavily.com


---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## 🎯 Available Use Cases

### 1. Basic Chatbot

A simple conversational AI assistant powered by Groq LLM.

### 2. Chatbot with Web Search

Enhances responses by fetching real-time information from the web using Tavily Search.

### 3. AI News Agent

Automatically gathers and summarizes the latest Artificial Intelligence news:

- Daily Summary
- Weekly Summary
- Monthly Summary
- Yearly Summary

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to your branch

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

