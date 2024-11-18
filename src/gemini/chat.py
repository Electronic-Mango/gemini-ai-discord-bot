from collections import defaultdict
from os import getenv

from dotenv import load_dotenv
from google.generativeai import GenerativeModel, configure

load_dotenv()

WELCOME_MESSAGE_REQUEST = "Show a welcome message explaining who you are and what you can do."
RATE_LIMIT_MESSAGE = "Rate limit reached, try again in 20s."

API_KEY = getenv("GEMINI_API_KEY")
MODEL = getenv("GEMINI_MODEL")
SYSTEM_PROMPT = getenv("GEMINI_SYSTEM_MESSAGE")
CONTEXT_LIMIT = getenv("GEMINI_CONTEXT_LIMIT")

configure(api_key=API_KEY)
model = GenerativeModel(MODEL)
chats = defaultdict(model.start_chat)


def initial_message() -> str | None:
    return model.generate_content(WELCOME_MESSAGE_REQUEST).text


def reset_conversation(channel_id: int) -> None:
    chats.pop(channel_id, None)


def next_message(
    channel_id: int, text: str, attachment_urls: list[str] = None, use_conversation: bool = True
) -> str:
    return chats[channel_id].send_message(text).text
