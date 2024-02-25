class Member:

    def __init__(self, data: dict):
        self.id: int = data["id"]
        self.balance: int = data["balance"]
