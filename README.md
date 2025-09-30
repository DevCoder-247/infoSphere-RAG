# infroSphere RAG: AI-Powered Document Processing System 🤖

infoSphere RAG is an AI-powered document processing system that allows users to upload and analyze various document types. It leverages a combination of Python libraries and Google's Generative AI to extract meaningful content, answer questions, and generate summaries from document data.

## 🌟 Key Features

  * **PDF & Image Processing:** Upload and process both PDF and image files, including scanned documents.
  * **AI-Powered Query Processing:** Use Google Generative AI in conjunction with LangChain to ask questions and get intelligent answers based on your documents.
  * **Vector Search:** Efficiently retrieve relevant information from documents using a FAISS vector store.
  * **Flexible Text Extraction:** The system uses PyMuPDF for native text extraction from PDFs and falls back to pytesseract (OCR) for scanned PDFs and images.
  * **Interactive Web Interface:** A user-friendly Gradio web interface makes it easy to upload files and interact with the AI assistant.
  * **Environment Variable Support:** Manage API keys and other configurations securely using a `.env` file.

## 🚀 How It Works

Documental operates by breaking down uploaded documents into smaller, meaningful chunks. These chunks are then converted into numerical representations called **embeddings** using a chosen model (either Google's `text-embedding-004` or a local Sentence Transformer model). These embeddings are stored in a FAISS vector database.

When you ask a question, the system converts your query into an embedding and searches the vector database for the most relevant document chunks. These chunks are then provided as context to a Google Generative AI model, which generates a concise, accurate answer based *only* on the provided information.

-----

## 💻 Setup Instructions

This guide will walk you through setting up the Documental project on your local machine.

### 1\. Prerequisites

  * **Python 3.10+** (or a later version)
  * **VS Code** (or another code editor of your choice)
  * A **Google API Key** for Generative AI access.

### 2\. Environment Setup

1.  **Clone the Repository:**

    ```bash
    git clone [repository_url]
    cd documental
    ```

2.  **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**

      * **On Windows:**
        ```bash
        venv\Scripts\activate
        ```
      * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure API Keys:**
    Create a file named `.env` in the root directory and add your Google API key.

    ```ini
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```

    > **Note:** The `EMBEDDING_BACKEND` can be set to `"gemini"` or `"minilm"`. Gemini embeddings require the `GOOGLE_API_KEY` to be configured. [cite\_start]The default setting is `"gemini"`[cite: 2].

### 3\. Running the Project

The project consists of a backend Flask API (`app.py`) and a frontend Gradio UI (`gradio_app.py`).

1.  **Start the Backend API:**
    Open a terminal and run the following command to start the Flask backend.

    ```bash
    python app.py
    ```

2.  **Start the Gradio UI:**
    Open a **second terminal** and run the following command to start the Gradio web interface.

    ```bash
    python gradio_app.py
    ```

3.  **Access the Application:**
    Open your web browser and navigate to the local address provided by Gradio, typically `http://127.0.0.1:7860`.

-----

## 🖼️ User Interface

### Home Screen

Upon launching, the Gradio UI provides a straightforward interface to check the backend status and upload documents.

### Upload Documents & Images

Use the **"Upload Files"** tab to drag and drop your PDF and image files. The system will process them and confirm the number of documents and chunks added to the vector store.

### Chat with Your Documents

Once files are indexed, switch to the **"Chat"** tab. You can ask questions and receive answers with citations directly from your uploaded documents.

-----

## 📚 Libraries and Technologies Used

| Library | Purpose |
| :--- | :--- |
| **Flask** | Backend API framework  |
| **Gradio** | Web interface for the application  |
| **LangChain** | AI & Large Language Model (LLM) integration  |
| **FAISS** | Vector database for storing document embeddings  |
| **PyMuPDF / pytesseract** | Used for extracting text from PDFs and images  |
| **Google Generative AI** | The core AI model for generating answers  |
| **Sentence Transformers** | Used for generating embeddings, including a local CPU-friendly model |

-----

## 🛠️ Common Issues

  * **Missing Modules:** If you encounter a `ModuleNotFoundError`, ensure all dependencies are installed by running `pip install -r requirements.txt`.
  * **Port Already in Use:** If the server fails to start because a port is already in use, you can change the port number in the `gradio_app.py` or `app.py` files.
  * **Dependency Conflicts:** If there are conflicts, try updating the `requirements.txt` file or reinstalling specific packages.

If you have questions or feedback, please open an issue in the project repository.
