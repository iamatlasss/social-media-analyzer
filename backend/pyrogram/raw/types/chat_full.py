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


class ChatFull(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ChatFull`.

    Details:
        - Layer: ``123``
        - ID: ``0xf3474af6``

    Parameters:
        id: ``int`` ``32-bit``
        about: ``str``
        participants: :obj:`ChatParticipants <pyrogram.raw.base.ChatParticipants>`
        notify_settings: :obj:`PeerNotifySettings <pyrogram.raw.base.PeerNotifySettings>`
        can_set_username (optional): ``bool``
        has_scheduled (optional): ``bool``
        chat_photo (optional): :obj:`Photo <pyrogram.raw.base.Photo>`
        exported_invite (optional): :obj:`ExportedChatInvite <pyrogram.raw.base.ExportedChatInvite>`
        bot_info (optional): List of :obj:`BotInfo <pyrogram.raw.base.BotInfo>`
        pinned_msg_id (optional): ``int`` ``32-bit``
        folder_id (optional): ``int`` ``32-bit``
        call (optional): :obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`
    """

    __slots__: List[str] = ["id", "about", "participants", "notify_settings", "can_set_username", "has_scheduled",
                            "chat_photo", "exported_invite", "bot_info", "pinned_msg_id", "folder_id", "call"]

    ID = 0xf3474af6
    QUALNAME = "types.ChatFull"

    def __init__(self, *, id: int, about: str, participants: "raw.base.ChatParticipants",
                 notify_settings: "raw.base.PeerNotifySettings", can_set_username: Union[None, bool] = None,
                 has_scheduled: Union[None, bool] = None, chat_photo: "raw.base.Photo" = None,
                 exported_invite: "raw.base.ExportedChatInvite" = None,
                 bot_info: Union[None, List["raw.base.BotInfo"]] = None, pinned_msg_id: Union[None, int] = None,
                 folder_id: Union[None, int] = None, call: "raw.base.InputGroupCall" = None) -> None:
        self.id = id  # int
        self.about = about  # string
        self.participants = participants  # ChatParticipants
        self.notify_settings = notify_settings  # PeerNotifySettings
        self.can_set_username = can_set_username  # flags.7?true
        self.has_scheduled = has_scheduled  # flags.8?true
        self.chat_photo = chat_photo  # flags.2?Photo
        self.exported_invite = exported_invite  # flags.13?ExportedChatInvite
        self.bot_info = bot_info  # flags.3?Vector<BotInfo>
        self.pinned_msg_id = pinned_msg_id  # flags.6?int
        self.folder_id = folder_id  # flags.11?int
        self.call = call  # flags.12?InputGroupCall

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ChatFull":
        flags = Int.read(data)

        can_set_username = True if flags & (1 << 7) else False
        has_scheduled = True if flags & (1 << 8) else False
        id = Int.read(data)

        about = String.read(data)

        participants = TLObject.read(data)

        chat_photo = TLObject.read(data) if flags & (1 << 2) else None

        notify_settings = TLObject.read(data)

        exported_invite = TLObject.read(data) if flags & (1 << 13) else None

        bot_info = TLObject.read(data) if flags & (1 << 3) else []

        pinned_msg_id = Int.read(data) if flags & (1 << 6) else None
        folder_id = Int.read(data) if flags & (1 << 11) else None
        call = TLObject.read(data) if flags & (1 << 12) else None

        return ChatFull(id=id, about=about, participants=participants, notify_settings=notify_settings,
                        can_set_username=can_set_username, has_scheduled=has_scheduled, chat_photo=chat_photo,
                        exported_invite=exported_invite, bot_info=bot_info, pinned_msg_id=pinned_msg_id,
                        folder_id=folder_id, call=call)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 7) if self.can_set_username else 0
        flags |= (1 << 8) if self.has_scheduled else 0
        flags |= (1 << 2) if self.chat_photo is not None else 0
        flags |= (1 << 13) if self.exported_invite is not None else 0
        flags |= (1 << 3) if self.bot_info is not None else 0
        flags |= (1 << 6) if self.pinned_msg_id is not None else 0
        flags |= (1 << 11) if self.folder_id is not None else 0
        flags |= (1 << 12) if self.call is not None else 0
        data.write(Int(flags))

        data.write(Int(self.id))

        data.write(String(self.about))

        data.write(self.participants.write())

        if self.chat_photo is not None:
            data.write(self.chat_photo.write())

        data.write(self.notify_settings.write())

        if self.exported_invite is not None:
            data.write(self.exported_invite.write())

        if self.bot_info is not None:
            data.write(Vector(self.bot_info))

        if self.pinned_msg_id is not None:
            data.write(Int(self.pinned_msg_id))

        if self.folder_id is not None:
            data.write(Int(self.folder_id))

        if self.call is not None:
            data.write(self.call.write())

        return data.getvalue()
