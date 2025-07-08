from telethon import TelegramClient, events

api_id = "api_id"
api_hash = "api_hash"

client = TelegramClient("assit_userbot", api_id, api_hash)

@client.on(events.NewMessage)
async def get_new_messages(event):
    await event.reply('Привет!')

async def main():
    me = await client.get_me()

    print(me.stringify())

    username = me.username
    print(username)
    print(me.phone)

    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)

    async for message in client.iter_messages('me'):
        print(message.id, message.text)

client.start()
client.run_until_disconnected()