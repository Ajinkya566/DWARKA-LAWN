import logging
from pathlib import Path

import streamlit as st
from agent import ask_agent


# Logging configuration
LOG_FILE = Path(__file__).parent / "app.log"

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


# Streamlit page configuration
st.set_page_config(
    page_title="METRO Sales Assistant Demo",
    page_icon="🛒",
    layout="centered",
)

st.title("🛒 METRO Sales Assistant Demo")

st.caption(
    "A local Agentic AI demo using sales data, "
    "RAG, LangGraph and Ollama."
)


# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# Display previous messages
for item in st.session_state.chat_history:
    with st.chat_message(item["role"]):
        st.write(item["content"])


# User input
question = st.chat_input(
    "Ask about sales or SOP documents..."
)


if question:
    # Save and display user message
    st.session_state.chat_history.append({
        "role": "user",
        "content": question,
    })

    with st.chat_message("user"):
        st.write(question)

    # Generate agent response
    with st.chat_message("assistant"):
        with st.spinner("Agent is thinking..."):
            try:
                logger.info("Agent request started")

                answer = ask_agent(question)

                logger.info(
                    "Agent request completed successfully"
                )

                st.write(answer)

                st.caption("Demo knowledge sources")
                st.write("- Sales data: data/sales_data.csv")
                st.write("- Sales SOP: data/sales_sop.txt")

                # Save assistant response
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": answer,
                })

            except Exception:
                logger.exception("Agent request failed")

                st.error(
                    "Something went wrong. "
                    "Please check app.log for details."
                )