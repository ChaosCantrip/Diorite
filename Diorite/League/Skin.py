class Skin:

    def __init__(self, data: dict):
        self.id: int = int(data["id"])
        self.num: int = data["num"]
        self.name: str = data["name"]
        self.has_chromas: bool = data["chromas"]
