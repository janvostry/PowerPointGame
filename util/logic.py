from model.entity.state import State
from model.enum.asset.message import Message
from model.enum.asset.sound import Sound
from model.enum.cell import Cell


class Logic:

    @staticmethod
    def iterate(prev_state: State, next_state: State) -> tuple[Sound, State, None | Message]:
        cell = next_state.level.grid[next_state.position.top][next_state.position.left]
        methods = {
            Cell.WALL: Logic.__iterate__wall,
            Cell.SPACE: Logic.__iterate__space,
            Cell.KEY: Logic.__iterate__key,
            Cell.LOCK: Logic.__iterate__lock,
            Cell.DOOR: Logic.__iterate__door,
            Cell.GEM: Logic.__iterate__gem,
            Cell.DRAGON: Logic.__iterate__dragon,
            Cell.PRINCESS: Logic.__iterate__princess,
        }
        if cell in methods:
            return methods[cell](prev_state, next_state)
        else:
            raise ValueError(f'Unhandled cell {cell}')

    @staticmethod
    def __iterate__wall(prev_state: State, _: State) -> tuple[Sound, State, None | Message]:
        return Sound.WALL_HIT, prev_state, None

    @staticmethod
    def __iterate__space(_: State, next_state: State) -> tuple[Sound, State, None | Message]:
        return Sound.FLOOR_WALK, next_state, None

    @staticmethod
    def __iterate__key(_: State, next_state: State) -> tuple[Sound, State, None | Message]:
        next_state = next_state.change(
                level=next_state.level.change(next_state.position, Cell.SPACE),
                inventory=next_state.inventory.change(keys=+1)
            )
        return Sound.KEY_PICKUP, next_state, None

    @staticmethod
    def __iterate__lock(prev_state: State, next_state: State) -> tuple[Sound, State, None | Message]:
        if next_state.inventory.keys >= 1:
            next_state = next_state.change(
                level=next_state.level.change(next_state.position, Cell.DOOR),
                inventory=next_state.inventory.change(keys=-1)
            )
            return Sound.DOOR_UNLOCK, next_state, None
        else:
            return Sound.DOOR_HIT, prev_state, Message.DOOR_LOCKED

    @staticmethod
    def __iterate__door(_: State, next_state: State) -> tuple[Sound, State, None | Message]:
        return Sound.FLOOR_WALK, next_state, None

    @staticmethod
    def __iterate__gem(_: State, next_state: State) -> tuple[Sound, State, None | Message]:
        next_state = next_state.change(
                level=next_state.level.change(next_state.position, Cell.SPACE),
                inventory=next_state.inventory.change(gems=+1)
            )
        return Sound.GEM_PICKUP, next_state, None

    @staticmethod
    def __iterate__dragon(prev_state: State, next_state: State) -> tuple[Sound, State, None | Message]:
        if next_state.inventory.gems >= 3:
            next_state = next_state.change(
                level=next_state.level.change(next_state.position, Cell.SPACE),
                inventory=next_state.inventory.change(gems=-3)
            )
            return Sound.DRAGON_ROAR, next_state, Message.DRAGON_BRIBE
        else:
            return Sound.DRAGON_ROAR, prev_state, Message.DRAGON_BLOCK

    @staticmethod
    def __iterate__princess(prev_state: State, _: State) -> tuple[Sound, State, None | Message]:
        return Sound.PRINCESS_LAUGH, prev_state, Message.PRINCESS_MESSAGE
