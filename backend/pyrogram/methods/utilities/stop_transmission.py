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

import pyrogram
from pyrogram.scaffold import Scaffold


class StopTransmission(Scaffold):
    def stop_transmission(self):
        """Stop downloading or uploading a file.

        This method must be called inside a progress callback function in order to stop the transmission at the
        desired time. The progress callback is called every time a file chunk is uploaded/downloaded.

        Example:
            .. code-block:: python
                :emphasize-lines: 9

                from pyrogram import Client

                app = Client("my_account")

                # Example to stop transmission once the upload progress reaches 50%
                # Useless in practice, but shows how to stop on command
                def progress(current, total, client):
                    if (current * 100 / total) > 50:
                        client.stop_transmission()

                with app:
                    app.send_document("me", "files.zip", progress=progress, progress_args=(app,))
        """
        raise pyrogram.StopTransmission
