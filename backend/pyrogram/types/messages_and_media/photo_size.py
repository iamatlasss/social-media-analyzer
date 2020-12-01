import pyrogram
from pyrogram import types, raw
from ..object import Object


class PhotoSize(Object):
    """
    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
            type: str = None,
            location: "types.FileLocation" = None,
            w: int = None,
            h: int = None,
            size: int = None,
    ):
        super().__init__(client=client)

        self.type = type
        self.location = location
        self.w = w
        self.h = h
        self.size = size

    @staticmethod
    def _parse(client, photo_size: "raw.types.PhotoSize"):
        if photo_size is None:
            return None
        return PhotoSize(
            client=client,

            type=getattr(photo_size, 'type', None),
            location=types.FileLocation._parse(client, getattr(photo_size, 'location', None)),
            w=getattr(photo_size, 'w', None),
            h=getattr(photo_size, 'h', None),
            size=getattr(photo_size, 'size', None),
        )
