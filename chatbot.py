from retriever import get_retriever
from langchain_ollama import OllamaLLM


def ask_question(question):

    retriever = get_retriever()

    docs = retriever.invoke(question)

    if not docs:
        return "I could not find this information in the uploaded documents."

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    llm = OllamaLLM(
        model="llama3.2:3b"
    )

    prompt = f"""
You are a RAG assistant.

Use ONLY the information present in the context.

If the answer is available in the context:
- Answer clearly.
- Give a detailed explanation.

If the answer is NOT available in the context, reply exactly:

I could not find this information in the uploaded documents.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.strip()


if __name__ == "__main__":

    print("Chatbot started (type 'exit' to stop)\n")

    while True:

        question = input("You: ")

        if question.lower() in ["exit", "quit"]:
            print("Chatbot stopped.")
            break

        answer = ask_question(question)

        print("\nAI:")
        print(answer)
        print()