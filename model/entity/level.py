import typing
from model.entity.position import Position
from model.enum.cell import Cell


class Level:

    def __init__(self, grid: list[list[Cell]]):
        self.__grid = grid

    @property
    def grid(self) -> list[list[Cell]]:
        return self.__grid

    def change(self, position: Position, replace: Cell) -> typing.Self:
        return Level(
            grid=[[
                cell if (left, top) != position else replace
                for left, cell in enumerate(line)
            ] for top, line in enumerate(self.__grid)]
        )
