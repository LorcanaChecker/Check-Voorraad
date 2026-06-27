import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"].strip()
import json

SUBSCRIBERS_FILE = "subscribers.json"


def load_subscribers():
    try:
        with open(SUBSCRIBERS_FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_subscribers(subscribers):
    with open(SUBSCRIBERS_FILE, "w") as f:
        json.dump(subscribers, f)


def add_subscriber(chat_id):
    subscribers = load_subscribers()

    if chat_id not in subscribers:
        subscribers.append(chat_id)
        save_subscribers(subscribers)


def remove_subscriber(chat_id):
    subscribers = load_subscribers()

    if chat_id in subscribers:
        subscribers.remove(chat_id)
        save_subscribers(subscribers)


def send_message(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    subscribers = load_subscribers()

    for chat_id in subscribers:

        requests.post(
            url,
            data={
                "chat_id": chat_id,
                "text": message
            },
            timeout=20
        )

    return True


def stock_message(shop, product, price, url, time):
    message = f"""🟢 OP VOORRAAD!

🏪 {shop}
📦 {product}

💶 {price}

🕒 {time}

🔗 {url}"""

    return send_message(message)


def soldout_message(shop, product, url, time):
    message = f"""🔴 UITVERKOCHT

🏪 {shop}
📦 {product}

🕒 {time}

🔗 {url}"""

    return send_message(message)


def price_message(shop, product, old_price, new_price, url, time):
    message = f"""💰 PRIJS GEWIJZIGD

🏪 {shop}
📦 {product}

{old_price} ➜ {new_price}

🕒 {time}

🔗 {url}"""

    return send_message(message)
