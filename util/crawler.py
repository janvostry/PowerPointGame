from model.entity.screen import MainScreen, Screen
from model.enum.button import Button
from util.logger import Logger


class Crawler:

    def __init__(self, levels: list[list[str]]):
        self.__screen = MainScreen(levels)
        self.__screens: dict[str, tuple[Screen, dict[Button, str]]] = {}

    @property
    def screens(self) -> dict[str, tuple[Screen, dict[Button, str]]]:
        return self.__screens

    def run(self) -> None:
        self.__screens = {}
        queue = [self.__screen]
        while len(queue) > 0:
            Logger.rewrite(f'Working: +{len(queue)} => #{len(self.__screens)} screens generated')
            if len(self.__screens) >= 1_000_000:
                raise RuntimeError('Too many screens, aborting')
            next_queue = {}
            for screen in queue:
                next_queue.update(self.__iterate(screen))
            queue = list(next_queue.values())
        Logger.write(f'Done: #{len(self.__screens)} screens generated')

    def __iterate(self, screen: Screen) -> dict[str, Screen]:
        queue = {}
        actions = {}
        for action in screen.actions:
            next_screen = screen.handle(action)
            next_hash = next_screen.get_hash()
            if next_hash not in self.__screens:
                queue[next_hash] = next_screen
            actions[action] = next_hash
        screen_hash = screen.get_hash()
        self.__screens[screen_hash] = (screen, actions)
        return queue
