from io import BytesIO
from typing import Iterable

from hikari import Attachment
from httpx import AsyncClient, codes


async def download_attachments(attachments: Iterable[Attachment]) -> list[tuple[BytesIO, str]]:
    return [file for attachment in attachments if (file := await _download_file(attachment.url))]


async def _download_file(url: str) -> tuple[BytesIO, str] | None:
    async with AsyncClient() as client:
        response = await client.get(url)
    content = BytesIO(response.content)
    mime_type = response.headers.get("content-type")
    return (content, mime_type) if codes.is_success(response.status_code) else None
