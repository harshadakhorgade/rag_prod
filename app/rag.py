from app.retrieval import retrieve_context
from app.llm import generate_answer


def rag_answer(question: str) -> str:
    chunks = retrieve_context(question, top_k=3)

    context = "\n\n".join(chunks)

    answer = generate_answer(context=context, question=question)

    return answer
