import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"].strip()

url = f"https://api.telegram.org/bot{BOT_TOKEN}/getMe"

print("URL:", url[:45] + "...")

response = requests.get(url)

print("Status:", response.status_code)
print("Response:", response.text)
