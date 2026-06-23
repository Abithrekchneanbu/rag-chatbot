import os
import pandas as pd

from langchain_core.documents import Document
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    CSVLoader
)

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings


def load_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    # PDF
    if ext == ".pdf":
        loader = PyPDFLoader(file_path)
        return loader.load()

    # TXT
    elif ext == ".txt":
        loader = TextLoader(file_path, encoding="utf-8")
        return loader.load()

    # CSV
    elif ext == ".csv":
        loader = CSVLoader(file_path)
        return loader.load()

    # Excel
    elif ext in [".xlsx", ".xls"]:
        df = pd.read_excel(file_path)

        text = df.to_string(index=False)

        return [Document(page_content=text)]

    else:
        raise ValueError(
            f"Unsupported file type: {ext}"
        )


def create_vector_db(file_paths):

    all_docs = []

    for file_path in file_paths:

        docs = load_file(file_path)

        all_docs.extend(docs)

    print(f"Loaded {len(all_docs)} documents")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(all_docs)

    print(f"Created {len(chunks)} chunks")

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    print("Vector DB created successfully")

    return vector_db


if __name__ == "__main__":

    file_paths = [
        "UNIT -5 -FDS.pdf"
    ]

    create_vector_db(file_paths)