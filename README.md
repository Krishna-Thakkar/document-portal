# 🧠 Document Portal

<div align="center">

**An intelligent document understanding system powered by RAG, LangChain, and FAISS**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-latest-green.svg)](https://langchain.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

[Features](#-features) • [Tech Stack](#-tech-stack) • [Setup](#-setup-instructions) • [Usage](#-usage) • [Project Structure](#-project-structure)

</div>

---

## 📋 Overview

**Document Portal** is a comprehensive document intelligence platform that leverages Retrieval-Augmented Generation (RAG) to provide three powerful document processing capabilities:

- **📊 Document Analysis** - Generate structured summaries and insights from uploaded documents
- **⚖️ Document Compare** - Perform detailed line-by-line comparisons between two documents
- **💬 Document Chat** - Interactive conversational interface for querying multiple documents simultaneously

Built with modern LLM technologies, Document Portal creates session-based FAISS indexes for efficient retrieval and supports multiple document formats including PDF, DOCX, and TXT files.

---

## ✨ Features

### 🎯 Core Capabilities

- **RAG-Based Document Understanding** - Combines retrieval and generation for accurate, context-aware responses
- **Multi-Document Support** - Process and query multiple documents in a single session
- **Session-Based Indexing** - FAISS indexes are created per session for optimal retrieval performance
- **Intelligent Document Comparison** - Identify differences and similarities between document versions
- **Structured Analysis** - Generate concise summaries with key insights and structured outputs

### 🏗️ Architecture & Design

- **Modular Codebase** - Clean separation of concerns with dedicated modules for ingestion, retrieval, analysis, and comparison
- **Custom Logging & Exception Handling** - Comprehensive logging system with custom exception handlers for debugging
- **YAML-Based Configuration** - Flexible configuration management through `config.yaml`
- **Persistent Storage** - Local storage of FAISS indexes and session metadata for quick retrieval
- **Streamlit UI** - User-friendly interface for seamless document interactions

### 📄 Supported Formats

- PDF documents (`.pdf`)
- Microsoft Word files (`.docx`)
- Plain text files (`.txt`)

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Language** | Python 3.10+ |
| **LLM Framework** | LangChain |
| **Vector Store** | FAISS (Facebook AI Similarity Search) |
| **Embeddings** | Google Embeddings |
| **LLM Models** | Google Gemini / Groq Models |
| **UI Framework** | Streamlit |
| **Architecture** | RAG (Retrieval-Augmented Generation) |
| **Configuration** | YAML |
| **Logging** | Custom Logger Module |

---

## 🚀 Setup Instructions

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/Krishna-Thakkar/document-portal.git
cd document-portal
```

2. **Create a virtual environment**

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

Create a `.env` file in the root directory and add your API keys:

```env
GOOGLE_API_KEY=your_google_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

5. **Update configuration** (Optional)

Modify `config/config.yaml` to customize model parameters, chunk sizes, and other settings.

### Running the Application

**Launch the Streamlit UI:**

```bash
streamlit run streamlit_ui.py
```

The application will open in your default browser at `http://localhost:8501`

---

## 💡 Usage

### 📊 Document Analysis

1. Navigate to the **Document Analysis** tab
2. Upload a document (PDF, DOCX, or TXT)
3. Click **Analyze** to generate a structured summary
4. Review the insights, key points, and analysis results

### ⚖️ Document Compare

1. Navigate to the **Document Compare** tab
2. Upload two versions of a document
3. Click **Compare** to generate a detailed comparison
4. Review highlighted differences and similarities

### 💬 Document Chat

1. Navigate to the **Document Chat** tab
2. Upload one or more documents
3. Wait for the FAISS index to be created
4. Ask questions about your documents in the chat interface
5. Receive contextually relevant answers with source citations

---

## 📁 Project Structure

```
document-portal/
│
├── api/                          # API endpoints
│   └── main.py
│
├── config/                       # Configuration files
│   └── config.yaml               # Model and system configurations
│
├── data/                         # Data storage
│   ├── document_analysis/        # Analyzed documents by session
│   ├── document_compare/         # Compared documents by session
│   └── multi_doc_chat/           # Sample documents for chat
│
├── exception/                    # Custom exception handling
│   └── custom_exception.py
│
├── faiss_index/                  # FAISS vector indexes by session
│   └── session_*/                # Session-specific indexes
│       ├── index.faiss
│       ├── index.pkl
│       └── ingested_meta.json
│
├── logger/                       # Logging utilities
│   └── custom_logger.py
│
├── logs/                         # Application logs
│
├── model/                        # Model definitions
│   └── models.py
│
├── notebook/                     # Jupyter notebooks for experiments
│   ├── experiments.ipynb
│   ├── logging_experiments.ipynb
│   └── exception_experiments.ipynb
│
├── prompt/                       # Prompt templates
│   └── prompt_library.py
│
├── src/                          # Core source code
│   ├── document_analyzer/        # Document analysis pipeline
│   │   └── data_analysis.py
│   ├── document_chat/            # RAG-based chat pipeline
│   │   └── retrieval.py
│   ├── document_compare/         # Document comparison pipeline
│   │   └── document_comparer.py
│   └── document_ingestion/       # Document loading and processing
│       └── data_ingestion.py
│
├── static/                       # Static assets
│   └── style.css
│
├── templates/                    # HTML templates
│   └── index.html
│
├── utils/                        # Utility functions
│   ├── config_loader.py          # Configuration loader
│   ├── document_ops.py           # Document operations
│   ├── file_io.py                # File I/O utilities
│   └── model_loader.py           # Model initialization
│
├── .gitignore                    # Git ignore rules
├── Dockerfile                    # Docker configuration
├── requirements.txt              # Python dependencies
├── setup.py                      # Package setup
├── streamlit_ui.py               # Streamlit application entry point
└── versions.py                   # Version information
```

---

## 🔧 Configuration

The `config/config.yaml` file allows you to customize:

- LLM model selection (Google Gemini, Groq, etc.)
- Embedding model parameters
- Chunk size and overlap for text splitting
- Temperature and other generation parameters
- FAISS index settings

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Krishna Thakkar**

- GitHub: [@Krishna-Thakkar](https://github.com/Krishna-Thakkar)
- Project Link: [https://github.com/Krishna-Thakkar/document-portal](https://github.com/Krishna-Thakkar/document-portal)

---

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) for the excellent LLM framework
- [FAISS](https://github.com/facebookresearch/faiss) for efficient similarity search
- [Streamlit](https://streamlit.io/) for the intuitive UI framework
- Google and Groq for their powerful LLM models

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ by Krishna Thakkar

</div>