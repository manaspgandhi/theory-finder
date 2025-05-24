from agent.research_agent import collect_theories
from llm.summarizer import summarize_theories

def main():
    query = input("Enter your TV show theory query: ")
    theories = collect_theories(query)
    summary = summarize_theories(theories, query)
    print("\nSummary of latest theories:")
    print(summary)

if __name__ == "__main__":
    main() 