import enum
import hashlib
import json
import typing
from model.entity.position import Position
from model.entity.state import State
from model.enum.asset.music import Music
from model.enum.asset.sound import Sound
from model.enum.button import Button
from model.enum.effect import Effect
from util.logic import Logic


class Screen:

    def __init__(self, actions: list[Button], sound: Sound, music: Music, effect: Effect):
        self.__actions = actions
        self.__sound = sound
        self.__music = music
        self.__effect = effect

    @property
    def actions(self) -> list[Button]:
        return self.__actions

    @property
    def sound(self) -> Sound:
        return self.__sound

    @property
    def music(self) -> Music:
        return self.__music

    @property
    def effect(self) -> Effect:
        return self.__effect

    def handle(self, button: Button) -> None | typing.Self:
        if button in self.__actions:
            raise NotImplementedError(f'Button {button} not handled on this screen')
        else:
            raise ValueError(f'Button {button} not supported on this screen')

    def get_hash(self) -> str:
        sponge = Screen.__get_dict(self)
        sponge = json.dumps(sponge, sort_keys=True).encode()
        sponge = hashlib.sha256(sponge)
        return sponge.hexdigest()

    @staticmethod
    def __get_dict(obj: object) -> object:
        if isinstance(obj, (bool, int, float, str)):
            return obj
        if isinstance(obj, enum.Enum):
            return obj.value
        if isinstance(obj, (list, tuple)):
            return [
                Screen.__get_dict(item)
                for item in obj
            ]
        if isinstance(obj, dict):
            return {
                key: Screen.__get_dict(value)
                for key, value in obj.items()
                if key != '_Screen__actions'
            }
        if hasattr(obj, '__dict__'):
            return Screen.__get_dict(vars(obj))
        raise TypeError(f'Cannot dictify {obj}')

class MainScreen(Screen):

    def __init__(self, levels: list[list[str]]):
        super().__init__([
            Button.PLAY,
        ], Sound.NONE, Music.THEME, Effect.NONE)
        self.__levels = levels

    @property
    def levels(self) -> list[list[str]]:
        return self.__levels

    def handle(self, button: Button) -> None | typing.Self:
        if button == Button.PLAY:
            state = State.create(self.levels[0])
            return MazeScreen(Sound.BUTTON_HIT, MazeScreen.EFFECT, state)
        else:
            super().handle(button)

class MazeScreen(Screen):

    EFFECT = Effect.FADE

    def __init__(self, sound: Sound, effect: Effect, state: State):
        super().__init__([
            Button.UP,
            Button.DOWN,
            Button.LEFT,
            Button.RIGHT,
        ], sound, Music.NONE, effect)
        self.__state = state

    @property
    def state(self) -> State:
        return self.__state

    def handle(self, button: Button) -> None | typing.Self:
        if button == Button.UP:
            return self.__move(Position(0, -1))
        elif button == Button.DOWN:
            return self.__move(Position(0, 1))
        elif button == Button.LEFT:
            return self.__move(Position(-1, 0))
        elif button == Button.RIGHT:
            return self.__move(Position(1, 0))
        else:
            super().handle(button)

    def __move(self, change: Position) -> None | typing.Self:
        next_state = self.state.change(
            position=change
        )
        sound, state, message = Logic.iterate(self.state, next_state)
        if message is not None:
            return DialogScreen(sound, state, message)
        else:
            return MazeScreen(sound, MazeScreen.EFFECT, state)

class DialogScreen(Screen):

    EFFECT = Effect.WIPE_UP

    def __init__(self, sound: Sound, state: State, message: str):
        super().__init__([
            Button.CLOSE
        ], sound, Music.NONE, DialogScreen.EFFECT)
        self.__state = state
        self.__message = message

    @property
    def state(self) -> State:
        return self.__state

    @property
    def message(self) -> str:
        return self.__message

    def handle(self, button: Button) -> None | typing.Self:
        if button == Button.CLOSE:
            return MazeScreen(Sound.BUTTON_HIT, DialogScreen.EFFECT, self.state)
        else:
            super().handle(button)
