import os
import csv
import requests
import json
import re
from dotenv import load_dotenv

load_dotenv()

STEAM_API_KEY = os.getenv("STEAM_API_KEY")
Helldivers2_ID = "553850"

Url = f"https://store.steampowered.com/appreviews/{Helldivers2_ID}"
params = {
    "json": "1",
    "num_per_page": "100",
    "filter": "recent",
}

# First iteration outside loop
response = requests.get(Url, params=params)
response_json = json.loads(response.content)
reviews = response_json["reviews"]
cursor = response_json["cursor"]

num_of_pages = 5
page = 0

while page < num_of_pages:
    Url = f"https://store.steampowered.com/appreviews/{Helldivers2_ID}"
    params = {
        "json": "1",
        "num_per_page": "100",
        "filter": "recent",
        "cursor": cursor,
    }
    response = requests.get(Url, params=params)
    response_json = json.loads(response.content)
    if "reviews" in response_json:
        reviews += response_json["reviews"]
        cursor = response_json["cursor"]
    else:
        print(f"response didnt include reviews at cursor{cursor}")
    page += 1

steam_info = ['received_for_free', 'steam_purchase', 'refunded', 'voted_up', 'timestamp_created', 'timestamp_updated', 'language', 'review']
with open('reviews.csv', 'w', newline='', encoding="utf-8-sig") as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',')
    csv_writer.writerow(steam_info)
    for review in reviews:
        row = [review.get(info, "") for info in steam_info[:-1]]
        filtered_review = re.sub(r'[^a-zA-Z0-9ąćęłńóśźżĄĆĘŁŃÓŚŹŻ\s]','',review['review'])
        filtered_review = filtered_review.replace('\n', '').replace('\r', '').strip()
        row.append(filtered_review)
        csv_writer.writerow(row)