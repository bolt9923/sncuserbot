from telethon import events
from userbot.main import client
from userbot.handlers.tagging import tag_running, tag_paused

@client.on(events.NewMessage(pattern=r"\.stoptag"))
async def stop(event):
    global tag_running
    tag_running = False
    await event.reply("⛔ Stopped")

@client.on(events.NewMessage(pattern=r"\.pausetag"))
async def pause(event):
    global tag_paused
    tag_paused = True
    await event.reply("⏸ Paused")

@client.on(events.NewMessage(pattern=r"\.resumetag"))
async def resume(event):
    global tag_paused
    tag_paused = False
    await event.reply("▶️ Resumed")
