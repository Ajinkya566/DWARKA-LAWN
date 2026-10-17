from pathlib import Path
from functools import lru_cache

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS


DATA_DIR = Path(__file__).parent / "data"
SOP_FILE = DATA_DIR / "sales_sop.txt"


@lru_cache(maxsize=1)
def create_vector_store():
    """Load SOP, split into chunks and create a local FAISS index."""

    if not SOP_FILE.exists():
        raise FileNotFoundError(
            f"SOP file not found: {SOP_FILE}"
        )

    loader = TextLoader(
        str(SOP_FILE),
        encoding="utf-8"
    )

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vector_store


def search_sop(question: str) -> str:
    """Search the sales SOP for relevant information."""

    try:
        vector_store = create_vector_store()

        results = vector_store.similarity_search_with_score(
            question,
            k=3
        )

        filtered_results = [
            (doc, score)
            for doc, score in results
            if score <= 1.0
        ]

        if not filtered_results:
            return "This information is not available in the provided SOP."

        context = "\n\n".join(
            doc.page_content
            for doc, score in filtered_results
        )

        return (
            "Retrieved information from sales_sop.txt:\n"
            f"{context}\n"
        )

    except Exception as error:
        return f"SOP search failed: {error}"