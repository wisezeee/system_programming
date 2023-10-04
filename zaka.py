import json
from time import sleep
import requests
from bs4 import BeautifulSoup


games = {}

for i in range(1, 16):
    zaka_zaka = 'https://zaka-zaka.com/game/new' + f"/page{i}"
    response = requests.get(zaka_zaka)
    print(zaka_zaka)
    if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            items = soup.find_all(class_='game-block')
            for item in items:
                if "game-block-more" in item.get("class"):
                    continue
                name = item.find(class_="game-block-name")
                price = item.find(class_="game-block-price")
                games[name.text] = {"price": float(price.text[:-1])}
    sleep(1)


with open("zaka_zaka.json", "w") as f:
    json.dump(games, f,  indent=4)