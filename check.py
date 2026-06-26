import os
import json
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"].strip()
CHAT_ID = os.environ["CHAT_ID"].strip()

PRODUCTS = {
    "Intertoys Wilds Unknown Booster": "https://www.intertoys.nl/disney-lorcana-tcg-wilds-unknown-sleeved-booster",
    "Bazaar Attack of the Vine Booster Box": "https://www.bazaarofmagic.eu/nl-NL/p/disney-lorcana-attack-of-the-vine-boosterbox-24-boosters/9161569",
    "TCG Family Wilds Unknown Booster Box": "https://www.tcgfamily.nl/en/products/disney-lorcana-wilds-unknown-boosterbox-24-boosters",
    "TCG Family Attack of the Vine Booster Box": "https://www.tcgfamily.nl/en/products/disney-lorcana-attack-of-the-vine-boosterbox-24-boosters-kopie-1",
    "TCG Family Wilds Unknown Booster": "https://www.tcgfamily.nl/en/products/disney-lorcana-wilds-unknown-booster",
    "TCG Family Attack of the Vine Trove": "https://www.tcgfamily.nl/en/products/disney-lorcana-attack-of-the-vine-illumineers-trove-kopie"
}

KEYWORDS = [
    "op voorraad",
    "in winkelwagen",
    "in stock",
    "add to cart",
    "buy now"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

try:
    with open("state.json", "r") as f:
        state = json.load(f)
except:
    state = {}

for name, url in PRODUCTS.items():
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
        text = r.text.lower()

        available = any(k in text for k in KEYWORDS)

        if available and not state.get(name, False):
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                data={
                    "chat_id": CHAT_ID,
                    "text": f"🎉 {name} lijkt op voorraad!\n{url}"
                }
            )
            state[name] = True

        elif not available:
            state[name] = False

    except Exception as e:
        print(name, e)

with open("state.json", "w") as f:
    json.dump(state, f)
