from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings


def get_retriever():

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    vector_db = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    retriever = vector_db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )

    return retriever


if __name__ == "__main__":

    print("Loading Retriever...")

    retriever = get_retriever()

    print("Retriever created successfully!")

    question = input("\nEnter a test question: ")

    docs = retriever.invoke(question)

    print(f"\nRetrieved {len(docs)} chunks\n")

    for i, doc in enumerate(docs, 1):

        print(f"\n========== CHUNK {i} ==========\n")

        print(doc.page_content[:1000])

        print("\n" + "=" * 50)