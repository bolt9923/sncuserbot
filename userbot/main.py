from telethon import TelegramClient
from userbot.config import API_ID, API_HASH, SESSION

client = TelegramClient(SESSION, API_ID, API_HASH)

# Import handlers
from userbot.handlers import tagging, controls, clone  # noqa

def start():
    client.start()
    print("🚀 Userbot Running...")
    client.run_until_disconnected()

if __name__ == "__main__":
    start()
