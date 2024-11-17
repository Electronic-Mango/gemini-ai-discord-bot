from typing import Sequence

from hikari import Attachment


def parse_image_urls(attachments: Sequence[Attachment]) -> list[str]:
    return [attachment.url for attachment in attachments]
