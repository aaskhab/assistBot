from telethon import TelegramClient, events

from db.queries import add_dialog

api_id = "api_id"
api_hash = "api_hash"

client = TelegramClient("assit_userbot", api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def get_new_messages(event):
    peer = await event.get_sender()
    peer_id = peer.id
    peer_username = peer.username
    text = event.raw_text

    await add_dialog(peer_id, peer_username, text, event.id)

client.start()
client.run_until_disconnected()