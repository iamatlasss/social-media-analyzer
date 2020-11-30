#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2020 Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Union, Any


# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class PageBlockBlockquote(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``117``
        - ID: ``0x263d7c26``

    Parameters:
        text: :obj:`RichText <pyrogram.raw.base.RichText>`
        caption: :obj:`RichText <pyrogram.raw.base.RichText>`
    """

    __slots__: List[str] = ["text", "caption"]

    ID = 0x263d7c26
    QUALNAME = "types.PageBlockBlockquote"

    def __init__(self, *, text: "raw.base.RichText", caption: "raw.base.RichText") -> None:
        self.text = text  # RichText
        self.caption = caption  # RichText

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "PageBlockBlockquote":
        # No flags

        text = TLObject.read(data)

        caption = TLObject.read(data)

        return PageBlockBlockquote(text=text, caption=caption)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.text.write())

        data.write(self.caption.write())

        return data.getvalue()
