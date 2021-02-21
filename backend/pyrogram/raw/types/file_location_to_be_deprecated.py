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


class FileLocationToBeDeprecated(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.FileLocation`.

    Details:
        - Layer: ``123``
        - ID: ``0xbc7fc6cd``

    Parameters:
        volume_id: ``int`` ``64-bit``
        local_id: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["volume_id", "local_id"]

    ID = 0xbc7fc6cd
    QUALNAME = "types.FileLocationToBeDeprecated"

    def __init__(self, *, volume_id: int, local_id: int) -> None:
        self.volume_id = volume_id  # long
        self.local_id = local_id  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "FileLocationToBeDeprecated":
        # No flags

        volume_id = Long.read(data)

        local_id = Int.read(data)

        return FileLocationToBeDeprecated(volume_id=volume_id, local_id=local_id)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags

        data.write(Long(self.volume_id))

        data.write(Int(self.local_id))

        return data.getvalue()
