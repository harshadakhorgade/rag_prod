import os
from groq import Groq

# Initialize Groq client using environment variable
# client = Groq(api_key=os.getenv("GROQ_API_KEY"))
client = Groq(api_key="GROQ_API_KEY")


def generate_answer(context: str, question: str) -> str:
    prompt = f"""
You are a helpful technical assistant.
Answer the question ONLY using the context below.
If the answer is not present in the context, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=300
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"LLM Error: {str(e)}"
