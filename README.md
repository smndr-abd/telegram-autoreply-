# Telegram Auto-Reply Bot

A simple Python script that logs into your personal Telegram account and automatically replies to private messages when you're away — similar to an "out of office" message.

Built with [Telethon](https://docs.telethon.dev/), which uses Telegram's MTProto API to act as your own account (not a separate bot account).

## Features

- Auto-replies to incoming **private messages** only (ignores groups/channels)
- Ignores messages from bots
- Replies to each sender **at most once every 6 hours**, to avoid spamming the same person repeatedly
- Keeps you logged in between runs via a saved session file

## Requirements

- Python 3.8+
- A Telegram account
- An `api_id` and `api_hash` from [my.telegram.org](https://my.telegram.org) → **API development tools**

## Setup

1. **Clone or copy this project** into a folder, e.g. `telegram-autoreply/`.

2. **Install dependencies:**
   ```bash
   pip install telethon
   ```
   (Use `pip3` / `python3` on macOS/Linux if `pip`/`python` aren't recognized.)

3. **Get your API credentials:**
   - Go to [my.telegram.org](https://my.telegram.org) and log in with your phone number.
   - Open **API development tools**.
   - Create an app (any title/short name, platform = Desktop or Other, URL field can be left blank or filled with a placeholder).
   - Copy the `api_id` and `api_hash`.

4. **Configure the script:**
   Open `autoreply.py` and fill in your credentials:
   ```python
   API_ID = 1234567
   API_HASH = "your_api_hash_here"
   REPLY = "Hey there! I'm not online right now, but I'll answer when I'm back."
   ```

5. **Run it:**
   ```bash
   python3 autoreply.py
   ```
   On first run, you'll be asked for:
   - Your **phone number** (with country code, e.g. `+998...`) — the account the bot will reply from
   - The **login code** Telegram sends you (usually via a message from the official Telegram app, not SMS)
   - Your **two-step verification password**, if you have one enabled

   After the first successful login, a `session.session` file is created so you won't need to log in again on future runs.

6. **Test it:**
   Have someone message the account directly. They should receive the auto-reply. Messaging your own Saved Messages won't trigger it.

## Project structure

```
telegram-autoreply/
├── autoreply.py       # main script
├── session.session    # created after first login — DO NOT share or commit
└── README.md
```

## Security notes

⚠️ **Keep these private — never commit or share them:**
- `session.session` — acts as a login to your account. Anyone with this file can access your account without needing a code or password.
- `api_hash` — your API credential.

If you believe your session file was exposed, go to **Telegram → Settings → Devices** and terminate the session immediately.

## Known limitations

- The script only replies while it's actively running. If your computer sleeps or shuts down, replies stop. For 24/7 uptime, run it on a server, VPS, or always-on device.
- It currently sends a fixed message to everyone — see **Roadmap** for planned improvements.
- Heavy automated messaging behavior (mass-replying to many new people, joining many groups) can trigger Telegram's anti-spam restrictions. This script's cooldown and private-message-only scope are designed to stay well within safe use.

## Roadmap

- [ ] Away/online toggle (e.g. via `/away` and `/back` commands sent to Saved Messages)
- [ ] LLM-powered replies instead of a fixed message
- [ ] Per-sender conversation history/context
- [ ] Time-based scheduling (only reply outside certain hours)
- [ ] Logging of incoming messages to a file or SQLite database
- [ ] Move secrets to a `.env` file instead of hardcoding them
- [ ] Deploy for 24/7 uptime (VPS, Raspberry Pi, etc.)

## Disclaimer

This script automates a **personal** Telegram account using Telethon (an unofficial client library). This is different from Telegram's official Bot API. Use responsibly and avoid behavior that could be mistaken for spam. Telegram Premium users may prefer the built-in **Away Messages** feature (Settings → Telegram Business) for a no-code, officially supported alternative.

## Created by Samandar Abdujabbar
