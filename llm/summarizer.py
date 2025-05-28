from typing import List, Dict

# TODO: Integrate with Gemini or OpenAI

def summarize_theories(theories: List[Dict], query: str) -> str:
    """Summarize the collected theories using an LLM."""
    # TODO: Implement LLM summarization
    return "Summary goes here." 

# CURL COMMAND
# curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${AIzaSyD9Vqbdbb62l_pvS2ZpV3RBxLSmnKF-oGM}" \
#   -H 'Content-Type: application/json' \
#   -X POST \
#   -d '{
#     "contents": [
#       {
#         "parts": [
#           {
#             "text": "Write a story about a magic backpack."
#           }
#         ]
#       }
#     ]
#   }'