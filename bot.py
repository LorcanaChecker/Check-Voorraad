import os
import json
import requests

from telegram import add_subscriber, remove_subscriber

BOT_TOKEN = os.environ["BOT_TOKEN"]

OFFSET_FILE = "offset.txt"


def load_offset():
    try:
        with open(OFFSET_FILE, "r") as f:
            return int(f.read().strip())
    except:
        return 0


def save_offset(offset):
    with open(OFFSET_FILE, "w") as f:
        f.write(str(offset))


offset = load_offset()

response = requests.get(
    f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates",
    params={"offset": offset, "timeout": 10},
    timeout=20
)

updates = response.json()

if updates["ok"]:

    for update in updates["result"]:

        update_id = update["update_id"]
        save_offset(update_id + 1)

        if "message" not in update:
            continue

        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "").strip().lower()

        if text == "/start":

            add_subscriber(chat_id)

            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                data={
                    "chat_id": chat_id,
                    "text": "✅ Je bent aangemeld voor Lorcana voorraadmeldingen!"
                },
                timeout=20
            )

        elif text == "/stop":

            remove_subscriber(chat_id)

            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                data={
                    "chat_id": chat_id,
                    "text": "❌ Je bent afgemeld voor Lorcana voorraadmeldingen."
                },
                timeout=20
            )
