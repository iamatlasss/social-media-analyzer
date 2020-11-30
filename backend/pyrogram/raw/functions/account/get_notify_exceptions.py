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


class GetNotifyExceptions(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``117``
        - ID: ``0x53577479``

    Parameters:
        compare_sound (optional): ``bool``
        peer (optional): :obj:`InputNotifyPeer <pyrogram.raw.base.InputNotifyPeer>`

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["compare_sound", "peer"]

    ID = 0x53577479
    QUALNAME = "functions.account.GetNotifyExceptions"

    def __init__(self, *, compare_sound: Union[None, bool] = None, peer: "raw.base.InputNotifyPeer" = None) -> None:
        self.compare_sound = compare_sound  # flags.1?true
        self.peer = peer  # flags.0?InputNotifyPeer

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetNotifyExceptions":
        flags = Int.read(data)

        compare_sound = True if flags & (1 << 1) else False
        peer = TLObject.read(data) if flags & (1 << 0) else None

        return GetNotifyExceptions(compare_sound=compare_sound, peer=peer)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.compare_sound is not None else 0
        flags |= (1 << 0) if self.peer is not None else 0
        data.write(Int(flags))

        if self.peer is not None:
            data.write(self.peer.write())

        return data.getvalue()
