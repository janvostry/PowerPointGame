import typing
from model.entity.inventory import Inventory
from model.entity.level import Level
from model.entity.position import Position
from model.enum.cell import Cell


class State:

    def __init__(self, level: Level, position: Position, inventory: Inventory):
        self.__level = level
        self.__position = position
        self.__inventory = inventory

    @property
    def level(self) -> Level:
        return self.__level

    @property
    def position(self) -> Position:
        return self.__position

    @property
    def inventory(self) -> Inventory:
        return self.__inventory

    def change(self, level: None | Level = None, position: None | Position = None, inventory: None | Inventory = None) -> typing.Self:
        return State(
            level=self.level if level is None else level,
            position=self.position + (position or Position(0, 0)),
            inventory=self.inventory if inventory is None else inventory
        )

    @staticmethod
    def create(level: list[str]) -> typing.Self:
        grid = [[
            Cell(cell)
            for cell in State.__grapheme_split(line)
        ] for line in level]
        grid, position = State.__extract_cell(grid, Cell.WIZARD, Cell.SPACE)
        return State(
            level=Level(grid=grid),
            position=position,
            inventory=Inventory(keys=0, gems=0)
        )

    @staticmethod
    def __grapheme_split(text: str) -> list[str]:
        result = []
        current = ''
        for char in text:
            if '\uFE00' <= char <= '\uFE0F':
                current += char
            else:
                if current:
                    result.append(current)
                current = char
        if current:
            result.append(current)
        return result

    @staticmethod
    def __extract_cell(grid: list[list[Cell]], search: Cell, replace: Cell) -> tuple[list[list[Cell]], Position]:
        for top, line in enumerate(grid):
            for left, cell in enumerate(line):
                if cell == search:
                    grid[top][left] = replace
                    return grid, Position(left, top)
        raise ValueError(f'Cannot find {search} in grid')
