import os

BOT_TOKEN = os.environ["BOT_TOKEN"].strip()

url = f"https://api.telegram.org/bot{BOT_TOKEN}/getMe"

print(url[:45] + "...")
