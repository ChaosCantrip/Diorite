from Diorite.League import Skin
from typing import Self


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

    @classmethod
    def get(cls, champion_id: str) -> Self:
        if champion_id in cls.champions_dict:
            return cls.champions_dict[champion_id]
        else:
            raise ValueError(f"Champion {champion_id} not found.")