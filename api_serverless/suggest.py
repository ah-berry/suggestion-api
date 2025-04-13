import os
from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage

load_dotenv()

# Uses two variations to obtain the api_key depending if the environment is ran locally or on Amazon Lambda
api_key = None
if os.environ.get("OPEN_API_KEY"):
    api_key = os.environ.get("OPEN_API_KEY")

if os.environ["OPEN_API_KEY"]:
    api_key = os.environ["OPEN_API_KEY"]

llm = OpenAI(
    model="gpt-3.5-turbo",
    api_key=api_key
)

PROMPT = ChatMessage(
    role="system",
    content=(
        "You are a mental health guidance counselor. You accept from the user, another mental health guidance counselor, "
        "information about the challenge(s) their patient is facing. Provide the user suggestion(s) on how to best help their "
        "patient. The suggestion(s) should be personalized to their patient's particular challenge(s) and contain actionable guidance. "
        "The tone and writing style of the suggestion(s) should be professional and considerate of the patient's circumstance(s)."
    )
)

def generate_suggestion(user_message: str) -> str:
    messages = [PROMPT, ChatMessage(role="user", content=user_message)]
    response = llm.chat(messages)
    return response.message.content
