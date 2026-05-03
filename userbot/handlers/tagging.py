import asyncio
import random
from telethon import events
from userbot.main import client
from telethon.tl.functions.messages import SendReactionRequest

tag_running = False
tag_paused = False

delay = 3
batch_size = 50

messages = [
    "Hello bro 👀",
    "Active ho kya?",
    "Reply karo 😎",
    "Kaun online hai?",
]
tag_styles = [
    "🔥 {name} {msg}",
    "⚡ {name} → {msg}",
    "👀 {name} | {msg}",
    "💀 {name} ❯ {msg}",
    "🚀 {name} >>> {msg}",
]
reactions = ["👍", "🔥", "❤️", "😂"]

@client.on(events.NewMessage(pattern=r"\.starttag"))
async def start_tag(event):
    global tag_running, tag_paused

    if tag_running:
        return await event.reply("Already running ⚠️")

    tag_running = True
    tag_paused = False

    users = await client.get_participants(event.chat_id)
    count = 0

    await event.reply("🚀 Tagging Started")

    for user in users:
        if not tag_running:
            break

        while tag_paused:
            await asyncio.sleep(2)

        if user.bot:
            continue

        name = user.first_name or "User"

        msg = await client.send_message(
            event.chat_id,
            f"[{name}](tg://user?id={user.id}) - {random.choice(messages)}",
            parse_mode="md"
        )

        count += 1

        try:
            await client(SendReactionRequest(
                peer=event.chat_id,
                msg_id=msg.id,
                reaction=[random.choice(reactions)]
            ))
        except:
            pass

        await asyncio.sleep(delay)

    tag_running = False
    await event.reply(f"✅ Done: {count}")
