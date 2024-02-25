from typing import Self


class Member:
    _list: list[Self] = []
    _dict: dict[int, Self] = {}

    def __init__(self, data: dict):
        self.id: int = data["id"]
        self.balance: int = data["balance"]
