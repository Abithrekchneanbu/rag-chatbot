<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a3a5c,100:63b3ed&height=220&section=header&text=RAG%20Chatbot&fontSize=65&fontColor=ffffff&fontAlignY=40&desc=Ask%20Questions%20About%20Your%20Documents&descAlignY=60&descSize=20&animation=fadeIn" width="100%"/>

<br/>

<a href="https://github.com/Abithrekchneanbu/rag-chatbot">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=22&pause=1000&color=63B3ED&center=true&vCenter=true&width=600&lines=Fully+Local+RAG+Pipeline+%F0%9F%A4%96;No+API+Keys+Required+%F0%9F%94%91;PDF+%E2%86%92+Chunks+%E2%86%92+Vectors+%E2%86%92+Answers;Powered+by+Llama+3.2+%2B+ChromaDB" alt="Typing SVG"/>
</a>

<br/><br/>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B35?style=for-the-badge&logo=databricks&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

<br/>

![GitHub stars](https://img.shields.io/github/stars/Abithrekchneanbu/rag-chatbot?style=social)
![GitHub forks](https://img.shields.io/github/forks/Abithrekchneanbu/rag-chatbot?style=social)
![GitHub issues](https://img.shields.io/github/issues/Abithrekchneanbu/rag-chatbot?color=blue&style=flat-square)
![Language](https://img.shields.io/github/languages/top/Abithrekchneanbu/rag-chatbot?style=flat-square&color=3776AB)

</div>

---

## 🧠 What is this?

> A **fully local** Retrieval-Augmented Generation chatbot. Upload PDF documents, ask questions in plain English, and get answers grounded strictly in your documents — no internet, no API keys, no data leaks.

---

## ✨ Features

<div align="center">

| 🏠 Fully Local | 📄 PDF Ingestion | 🔎 Semantic Search |
|:-:|:-:|:-:|
| Runs 100% on your machine. Zero external calls. | Upload any PDF — auto-chunked and embedded. | ChromaDB finds the most relevant chunks. |

| 🛡️ Grounded Answers | 🎛️ Streamlit UI | 🔌 Modular Design |
|:-:|:-:|:-:|
| LLM answers only from retrieved context. | Clean browser chat — no frontend skills needed. | Swap models, loaders, or retriever easily. |

</div>

---

## 🏗️ Architecture

<div align="center">

```
┌─────────────────────────────────────────────────────────────┐
│                      RAG PIPELINE                           │
│                                                             │
│   📄 PDFs                                                   │
│     │                                                       │
│     ▼                                                       │
│  ┌──────────┐    ┌──────────────┐    ┌──────────────────┐  │
│  │loaders.py│───▶│  LangChain   │───▶│    ChromaDB      │  │
│  │          │    │chunk + embed │    │  vector store    │  │
│  └──────────┘    └──────────────┘    └────────┬─────────┘  │
│                                               │             │
│                                    semantic retrieval       │
│                                               │             │
│                                               ▼             │
│                                    ┌──────────────────┐    │
│                                    │  retriever.py    │    │
│                                    │  (top-k chunks)  │    │
│                                    └────────┬─────────┘    │
│                                             │               │
│                                    context + question       │
│                                             │               │
│                                             ▼               │
│                                    ┌──────────────────┐    │
│                                    │   chatbot.py     │    │
│                                    │  Llama 3.2 (3B)  │    │
│                                    │   via Ollama     │    │
│                                    └────────┬─────────┘    │
│                                             │               │
│                                             ▼               │
│                                    ┌──────────────────┐    │
│                                    │ streamlit_app.py │    │
│                                    │    Web Chat UI   │    │
│                                    └──────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

</div>

---

## 🛠️ Tech Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=python,git,github&theme=dark" />

| Layer | Tool | Role |
|---|---|---|
| **Language** | Python 3.10+ | Core runtime |
| **LLM Framework** | LangChain + langchain-ollama | Orchestration & chaining |
| **Local LLM** | Llama 3.2 (3B) via Ollama | Answer generation |
| **Vector Store** | ChromaDB | Embedding storage & retrieval |
| **UI** | Streamlit | Web chat interface |
| **Document Loader** | LangChain PDF Loaders | PDF parsing & chunking |

</div>

---

## 📁 Project Structure

```
rag-chatbot/
│
├── 🐍 chatbot.py           ← Core RAG logic: retrieves context, calls LLM
├── 🐍 loaders.py           ← PDF loading and text chunking
├── 🐍 retriever.py         ← ChromaDB vector search
├── 🐍 streamlit_app.py     ← Browser-based chat UI
│
├── 📁 chroma_db/           ← Auto-generated vector store (git-ignored)
│
├── 📄 UNIT -5 -FDS.pdf                              ← Sample document
└── 📄 Visualizing errors, Density and Contour.pdf   ← Sample document
```

---

## 🚀 Quick Start

### Prerequisites

- 🐍 Python 3.10+
- 🦙 [Ollama](https://ollama.com) installed and running

### Step 1 — Clone

```bash
git clone https://github.com/Abithrekchneanbu/rag-chatbot.git
cd rag-chatbot
```

### Step 2 — Install dependencies

```bash
pip install langchain langchain-ollama chromadb streamlit
```

### Step 3 — Pull the local model

```bash
ollama pull llama3.2:3b
```

### Step 4 — Launch

**🌐 Web UI (recommended)**
```bash
streamlit run streamlit_app.py
```

**💻 Terminal chatbot**
```bash
python chatbot.py
```

---

## 💬 How It Works

```python
# chatbot.py — simplified flow
from retriever import get_retriever
from langchain_ollama import OllamaLLM

def ask_question(question):
    retriever = get_retriever()
    docs = retriever.invoke(question)          # 🔍 semantic search
    context = "\n\n".join([d.page_content      # 📄 build context
                           for d in docs])

    llm = OllamaLLM(model="llama3.2:3b")      # 🦙 local LLM

    prompt = f"""
    Use ONLY the context below to answer.
    If the answer is not there, say so.

    Context: {context}
    Question: {question}
    """
    return llm.invoke(prompt).strip()          # 💬 grounded answer
```

---

## 🤝 Contributing

```bash
# 1 — Fork & clone
gh repo fork Abithrekchneanbu/rag-chatbot --clone

# 2 — Create a branch
git checkout -b feat/your-feature

# 3 — Make changes and commit
git add .
git commit -m "feat: describe your change"

# 4 — Push and open a PR
git push origin feat/your-feature
gh pr create --title "Your feature"
```

All contributions welcome — bug fixes, new document loaders, model swaps, UI improvements!

---

## 📜 License

This project is open source. See [LICENSE](LICENSE) for details.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:63b3ed,100:0d1117&height=130&section=footer" width="100%"/>

**Built by [Abithrekchneanbu](https://github.com/Abithrekchneanbu)**

*If this helped you, please consider giving it a ⭐!*

</div>
