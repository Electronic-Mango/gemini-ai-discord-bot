from collections import defaultdict, namedtuple
from os import getenv

from dotenv import load_dotenv
from google.generativeai import GenerativeModel, configure

load_dotenv()

Message = namedtuple("Message", ["role", "content"])

WELCOME_MESSAGE = "Show a welcome message explaining who you are and what you can do."
RATE_LIMIT_MESSAGE = "Rate limit reached, try again in 20s."

API_KEY = getenv("GEMINI_API_KEY")
MODEL = getenv("GEMINI_MODEL")
SYSTEM_PROMPT = getenv("GEMINI_SYSTEM_MESSAGE")
CONTEXT_LIMIT = getenv("GEMINI_CONTEXT_LIMIT")

configure(api_key=API_KEY)
model = GenerativeModel(MODEL)
conversations = defaultdict(model.start_chat)


async def initial_message(channel_id: int) -> str | None:
    return await next_message(channel_id, WELCOME_MESSAGE, use_conversation=False)


def reset_conversation(channel_id: int) -> None:
    conversations.pop(channel_id, None)


async def next_message(
    channel_id: int, text: str, attachment_urls: list[str] = None, use_conversation: bool = True
) -> str:
    pass
