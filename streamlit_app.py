import streamlit as st
from loaders import create_vector_db
from chatbot import ask_question

st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 RAG Chatbot")

# Session State
if "db_ready" not in st.session_state:
    st.session_state.db_ready = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# Upload Files
uploaded_files = st.file_uploader(
    "Upload PDF, TXT, CSV, XLSX files",
    type=["pdf", "txt", "csv", "xlsx", "xls"],
    accept_multiple_files=True
)

if uploaded_files:

    file_paths = []

    for uploaded_file in uploaded_files:

        file_path = uploaded_file.name

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        file_paths.append(file_path)

    if st.button("Build Knowledge Base"):

        with st.spinner("Creating Vector Database..."):

            create_vector_db(file_paths)

        st.session_state.db_ready = True

        st.success("Vector DB Created Successfully!")


# Chat Section
if st.session_state.db_ready:

    st.subheader("💬 Chat with your Documents")

    user_question = st.chat_input(
        "Ask a question about your documents..."
    )

    if user_question:

        # Save user message
        st.session_state.chat_history.append(
            ("user", user_question)
        )

        # Get RAG Answer
        answer = ask_question(user_question)

        # Save AI message
        st.session_state.chat_history.append(
            ("assistant", answer)
        )

    # Display Chat History
    for role, message in st.session_state.chat_history:

        with st.chat_message(role):
            st.write(message)

else:

    st.info(
        "Upload files and click 'Build Knowledge Base' to start chatting."
    )