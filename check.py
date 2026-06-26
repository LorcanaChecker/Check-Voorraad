from datetime import datetime

from shops import intertoys, bazaar, tcgfamily
from telegram import stock_message, soldout_message, price_message
from state import load_state, save_state, get_product, set_product

PRODUCTS = [
    {
        "key": "intertoys_booster",
        "shop": "Intertoys",
        "product": "Wilds Unknown Sleeved Booster",
        "url": "https://www.intertoys.nl/disney-lorcana-tcg-wilds-unknown-sleeved-booster",
        "checker": intertoys
    },
    {
        "key": "bazaar_box",
        "shop": "Bazaar of Magic",
        "product": "Attack of the Vine Booster Box",
        "url": "https://www.bazaarofmagic.eu/nl-NL/p/disney-lorcana-attack-of-the-vine-boosterbox-24-boosters/9161569",
        "checker": bazaar
    },
    {
        "key": "tcg_box",
        "shop": "TCG Family",
        "product": "Attack of the Vine Booster Box",
        "url": "https://www.tcgfamily.nl/en/products/disney-lorcana-attack-of-the-vine-boosterbox-24-boosters-kopie-1",
        "checker": tcgfamily
    },
    {
        "key": "tcg_trove",
        "shop": "TCG Family",
        "product": "Attack of the Vine Illumineer's Trove",
        "url": "https://www.tcgfamily.nl/en/products/disney-lorcana-attack-of-the-vine-illumineers-trove-kopie",
        "checker": tcgfamily
    }
]

state = load_state()

checked = 0
available = 0
changed = 0

now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

for item in PRODUCTS:

    checked += 1

    try:

        result = item["checker"](item["url"])

        current = get_product(state, item["key"])

        if result["available"]:
            available += 1

        if result["available"] != current["available"]:

            changed += 1

            if result["available"]:

                stock_message(
                    item["shop"],
                    item["product"],
                    result["price"],
                    item["url"],
                    now
                )

            else:

                soldout_message(
                    item["shop"],
                    item["product"],
                    item["url"],
                    now
                )

        elif result["price"] != current["price"]:

            if result["price"] != "Onbekend":

                changed += 1

                price_message(
                    item["shop"],
                    item["product"],
                    current["price"],
                    result["price"],
                    item["url"],
                    now
                )

        set_product(
            state,
            item["key"],
            result["available"],
            result["price"]
        )

    except Exception as e:

        print(item["shop"], e)

save_state(state)

print()

print("====================================")
print("Controle voltooid")
print("------------------------------------")
print("Winkels:", checked)
print("Op voorraad:", available)
print("Wijzigingen:", changed)
print("Tijd:", now)
print("====================================")
