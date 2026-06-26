import requests
from bs4 import BeautifulSoup
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def get_price(text):
    prices = re.findall(r'€\s?[0-9.,]+', text)
    return prices[0] if prices else "Onbekend"


def intertoys(url):
    r = requests.get(url, headers=HEADERS, timeout=20)
    soup = BeautifulSoup(r.text, "html.parser")

    text = soup.get_text(" ", strip=True)

    available = (
        "in winkelmand" in text.lower()
        or "toevoegen aan winkelwagen" in text.lower()
        or "op voorraad" in text.lower()
    )

    return {
        "available": available,
        "price": get_price(text)
    }


def bazaar(url):
    r = requests.get(url, headers=HEADERS, timeout=20)
    soup = BeautifulSoup(r.text, "html.parser")

    text = soup.get_text(" ", strip=True)

    available = (
        "add to cart" in text.lower()
        or "in stock" in text.lower()
        or "op voorraad" in text.lower()
    )

    return {
        "available": available,
        "price": get_price(text)
    }


def tcgfamily(url):
    r = requests.get(url, headers=HEADERS, timeout=20)
    soup = BeautifulSoup(r.text, "html.parser")

    text = soup.get_text(" ", strip=True)

    available = (
        "add to cart" in text.lower()
        or "buy now" in text.lower()
        or "in stock" in text.lower()
    )

    return {
        "available": available,
        "price": get_price(text)
    }
