from app.rag import rag_answer

query = "What is Docker and why is it used?"
answer = rag_answer(query)

print("\nANSWER:\n")
print(answer)
