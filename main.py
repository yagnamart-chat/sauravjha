import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.errors import UserAlreadyParticipantError, ChannelInvalidError

# Environment Variables se details uthayega
api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
session_string = os.environ.get("SESSION_STRING")

# 📌 Groups ki list - jitne chahe utne add karo
GROUP_USERNAMES = [
    "delhi_university_students",  # https://t.me/delhi_university_students
    # "doosra_group_username",    # Aise aur groups add kar sakte ho
    # "teesra_group_username"
]

if not session_string:
    print("ERROR: SESSION_STRING nahi mili! Pehle string generate karo.")
    exit(1)

client = TelegramClient(StringSession(session_string), int(api_id), api_hash)

# Group join karne ka function (ab ek se zyada groups join karega)
async def join_groups():
    print("🔄 Groups mein join ho raha hoon...")
    for username in GROUP_USERNAMES:
        try:
            print(f"📌 Trying: {username}")
            entity = await client.get_entity(username)
            await client.join_channel(entity)
            print(f"✅ Joined: {username}")
        except UserAlreadyParticipantError:
            print(f"ℹ️ Already joined: {username}")
        except ChannelInvalidError:
            print(f"❌ Invalid group: {username}")
        except Exception as e:
            print(f"⚠️ Error joining {username}: {e}")
    print("✅ Group joining process complete.")

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply('Bhai, tera bot Zinda hai! 🚀')

async def main():
    await client.start()
    print("🤖 Bot start ho gaya!")
    
    # Saare groups join karo
    await join_groups()
    
    print("📡 Messages sun raha hoon...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
