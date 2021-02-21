#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2021 Dan <https://github.com/delivrance>
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


class Report(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``123``
        - ID: ``0xbd82b658``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        id: List of ``int`` ``32-bit``
        reason: :obj:`ReportReason <pyrogram.raw.base.ReportReason>`

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "id", "reason"]

    ID = 0xbd82b658
    QUALNAME = "functions.messages.Report"

    def __init__(self, *, peer: "raw.base.InputPeer", id: List[int], reason: "raw.base.ReportReason") -> None:
        self.peer = peer  # InputPeer
        self.id = id  # Vector<int>
        self.reason = reason  # ReportReason

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "Report":
        # No flags

        peer = TLObject.read(data)

        id = TLObject.read(data, Int)

        reason = TLObject.read(data)

        return Report(peer=peer, id=id, reason=reason)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(self.peer.write())

        data.write(Vector(self.id, Int))

        data.write(self.reason.write())

        return data.getvalue()
