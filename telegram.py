import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"].strip()
CHAT_ID = os.environ["CHAT_ID"].strip()


def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message
        },
        timeout=20
    )

    return response.status_code == 200


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
