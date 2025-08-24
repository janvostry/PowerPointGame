import typing


class Inventory:

    def __init__(self, keys: int, gems: int):
        self.__keys = keys
        self.__gems = gems

    @property
    def keys(self) -> int:
        return self.__keys

    @property
    def gems(self) -> int:
        return self.__gems

    def change(self, keys: None | int = None, gems: None | int = None) -> typing.Self:
        return Inventory(
            keys=self.keys + (keys or 0),
            gems=self.gems + (gems or 0)
        )
