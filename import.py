from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.types import *

# https://tl.telethon.dev/index.html


with TelegramClient('sessions/import', 6, 'AAFUWQhmtUtW-u1xX1dF_YX56K-ByrXl9sA') as client:
    client.get_dialogs()
    chat = client.get_entity(PeerUser(11376009)) # put user id

    result = client(functions.messages.InitHistoryImportRequest(
        peer=chat,
        file=client.upload_file('C:\\export\\a.txt'),
        media_count=0
    ))
    print(result.stringify())
    result = client(functions.messages.StartHistoryImportRequest(
        peer=chat,
        import_id=result.id
    ))
    print(result)
