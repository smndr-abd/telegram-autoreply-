import time
from telethon import TelegramClient, events

API_ID = 12345678 # must add your own api id          # from my.telegram.org
API_HASH = "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6" # must add your own api hash
REPLY = "Hey there! I'm not online right now but I'll answer when I'm back."
COOLDOWN = 6 * 3600          # reply to each person at most once per 6 hours


client = TelegramClient("session", API_ID, API_HASH)
last_replied = {}

@client.on(events.NewMessage(incoming=True))
async def auto_reply(event):
    if not event.is_private:          # ignore groups and channels
        return
    sender = await event.get_sender()
    if sender is None or sender.bot:  # ignore bots
        return
    now = time.time()
    if now - last_replied.get(sender.id, 0) < COOLDOWN:
        return
    last_replied[sender.id] = now
    await event.reply(REPLY)

client.start()  # first run asks for your phone number and login code
client.run_until_disconnected()