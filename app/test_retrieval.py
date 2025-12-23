# from retrieval import retrieve_context
from app.retrieval import retrieve_context

if __name__ == "__main__":
    query = "What is Docker and why is it used?"
    print(f"\nQuery: {query}\n")

    results = retrieve_context(query, top_k=5)

    if not results:
        print("No results found.")
    else:
        print("Top retrieved chunks:\n")
        for i, chunk in enumerate(results, 1):
            print(f"{i}. {chunk[:300]}...\n")
