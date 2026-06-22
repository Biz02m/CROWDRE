import os

import requests
from dotenv import load_dotenv
load_dotenv()

STEAM_API_KEY = os.getenv("STEAM_API_KEY")

Helldivers2_ID = "553850"
cursor = ""
Url = f"https://store.steampowered.com/appreviews/{Helldivers2_ID}?json=1&num_per_page=100&filter=recent&{cursor}"


Response = requests.get(Url)

print(Response.content)