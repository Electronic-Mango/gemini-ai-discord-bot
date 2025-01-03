from os import getenv
from typing import Awaitable, Callable

from dotenv import load_dotenv
from mdformat import text
from simplemarkdownsplitter import split

load_dotenv()
MAX_MESSAGE_LENGTH = int(getenv("MAX_MESSAGE_LENGTH", 2000))


async def send(message: str, sender: Callable[[str], Awaitable[None]]) -> None:
    chunks = split(text(message, options={"number": True}), MAX_MESSAGE_LENGTH, force=True)
    for chunk in chunks:
        await sender(chunk)
