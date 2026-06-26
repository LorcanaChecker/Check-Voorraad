import json
import os

STATE_FILE = "state.json"


def load_state():
    if not os.path.exists(STATE_FILE):
        return {}

    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}


def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)


def get_product(state, key):
    return state.get(
        key,
        {
            "available": False,
            "price": None
        }
    )


def set_product(state, key, available, price):
    state[key] = {
        "available": available,
        "price": price
    }
