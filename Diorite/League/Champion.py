from Diorite.League import Skin


class Champion:

    def __init__(self, data: dict):
        self.id: str = data["id"]
        self.key: int = int(data["key"])
        self.name: str = data["name"]
        self.title: str = data["title"]
        self.image_url: str = r"https://ddragon.leagueoflegends.com/cdn/14.5.1/data/en_US/champion/" + data["id"] + ".png"
        self.skins: list[Skin] = [Skin(skin) for skin in data["skins"]]
