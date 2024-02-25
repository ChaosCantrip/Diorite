from typing import Self


class Member:
    _list: list[Self] = []
    _dict: dict[int, Self] = {}

    def __init__(self, data: dict):
        self.id: int = data["id"]
        self.balance: int = data["balance"]

    # ===== Class Methods =====

    @classmethod
    def get(cls, member_id: int, create: bool = True) -> Self:
        """
        Get a member by their ID.

        :param member_id: ID of the member to get.
        :param create: Whether to create the member if they don't exist.
        :return: The member with the given ID.
        """
        if member_id in cls._dict:
            return cls._dict[member_id]
        elif create:
            return cls._create(member_id)
        else:
            raise ValueError(f"Member {member_id} not found.")

    @classmethod
    def _create(cls, member_id: int) -> Self:
        """
        Create a new member.

        :param member_id: ID of the member to create.
        :return: The new member.
        """
        member = cls({"id": member_id, "balance": 0})
        cls._list.append(member)
        cls._dict[member_id] = member
        return member
