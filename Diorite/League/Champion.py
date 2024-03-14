from Diorite.League import Skin
from typing import Self
import json
import os

CHAMPIONS_JSON_PATH = "data/live/league/champions.json"
CHAMPIONS_FOLDER_PATH = "data/live/league/champions"

if not os.path.exists(CHAMPIONS_FOLDER_PATH):
    os.makedirs(CHAMPIONS_FOLDER_PATH)


class Champion:
    champions = []
    champions_dict = {}

    def __init__(self, data: dict):
        self.id: str = data["id"]
        self.key: int = int(data["key"])
        self.name: str = data["name"]
        self.title: str = data["title"]
        self.image_url: str = r"https://ddragon.leagueoflegends.com/cdn/14.5.1/data/en_US/champion/" + data["id"] + ".png"
        self.skins: list[Skin] = [Skin(skin) for skin in data["skins"]]

    def __repr__(self):
        return f"<Champion {self.key}: {self.name}>"

    @classmethod
    def get(cls, champion_id: str) -> Self:
        champion_id = champion_id.lower()
        if champion_id in cls.champions_dict:
            return cls.champions_dict[champion_id]
        else:
            raise ValueError(f"Champion {champion_id} not found.")

    @classmethod
    def load_champions(cls) -> None:
        cls.champions.clear()
        cls.champions_dict.clear()
        for filename in os.listdir(CHAMPIONS_FOLDER_PATH):
            if filename.endswith(".json"):
                with open(f"{CHAMPIONS_FOLDER_PATH}/{filename}", "r") as f:
                    data = json.load(f)
                    champion = cls(data["data"])
                    cls.champions.append(champion)
                    cls.champions_dict[champion.id.lower()] = champion



Champion.load_champions()
print("Here")
for champion in Champion.champions:
    print(champion)
    for skin in champion.skins:
        print("\t" + skin)
