from telethon import events
from userbot.main import client
from telethon.tl.functions.account import UpdateProfileRequest

@client.on(events.NewMessage(pattern=r"\.clone"))
async def clone(event):
    if not event.is_reply:
        return await event.reply("Reply to user")

    user = await event.get_reply_message()
    user = await user.get_sender()

    await client(UpdateProfileRequest(
        first_name=user.first_name or "",
        last_name=user.last_name or ""
    ))

    await event.reply("✅ Cloned")
