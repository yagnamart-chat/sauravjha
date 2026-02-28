import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# Environment Variables se details uthayega
api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
session_string = os.environ.get("SESSION_STRING")

if not session_string:
    print("ERROR: SESSION_STRING nahi mili! Pehle string generate karo.")
else:
    client = TelegramClient(StringSession(session_string), int(api_id), api_hash)

    @client.on(events.NewMessage(pattern='/start'))
    async def start(event):
        await event.reply('Bhai, tera bot Zinda hai! 🚀')

    print("Bot start ho raha hai...")
    client.start()
    client.run_until_disconnected()
