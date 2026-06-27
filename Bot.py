import os
import requests

from telegram import add_subscriber, remove_subscriber

BOT_TOKEN = os.environ["BOT_TOKEN"]

url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

response = requests.get(url, timeout=20)

updates = response.json()

if updates["ok"]:

    for update in updates["result"]:

        if "message" not in update:
            continue

        chat_id = update["message"]["chat"]["id"]

        text = update["message"].get("text", "")

        if text == "/start":

            add_subscriber(chat_id)

            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                data={
                    "chat_id": chat_id,
                    "text": "✅ Je bent aangemeld voor Lorcana voorraadmeldingen!"
                }
            )

        elif text == "/stop":

            remove_subscriber(chat_id)

            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                data={
                    "chat_id": chat_id,
                    "text": "❌ Je bent afgemeld."
                }
            )
