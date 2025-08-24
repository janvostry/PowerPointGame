import typing


class Position:

    def __init__(self, left: int, top: int):
        self.__left = left
        self.__top = top

    @property
    def left(self) -> int:
        return self.__left

    @property
    def top(self) -> int:
        return self.__top

    def __add__(self, other: 'Position') -> typing.Self:
        return Position(
            left=self.left + other.left,
            top=self.top + other.top
        )

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Position):
            return (self.left, self.top) == (other.left, other.top)
        elif isinstance(other, tuple) and len(other) == 2 and all(isinstance(x, int) for x in other):
            return (self.left, self.top) == other
        else:
            raise NotImplementedError()
