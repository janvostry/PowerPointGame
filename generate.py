from model.enum.asset.message import Message
from model.enum.asset.music import Music
from model.enum.asset.sound import Sound
from model.enum.button import Button
from model.enum.cell import Cell
from util.composer import Composer
from util.crawler import Crawler
from util.logger import Logger


def main():
    # -m pip install types-lxml python-pptx
    # https://www.youtube.com/watch?v=SmYDGnwg4dA
    # https://docs.google.com/presentation/d/e/2PACX-1vRyCXoamwjJQ2_o-ugeYXrRm_ZXs7WZZP3BldGfEPfQ5SqXgXmRlUJAvpLuOYAtqSVRkX3hskZS-GzZ/pub?start=false&loop=false
    crawler = Crawler(levels=LEVELS)
    crawler.run()
    composer = Composer(
        ASSETS,
        len(LEVELS[0][0]) + 6,
        len(LEVELS[0]) + 2,
    )
    composer.prepare(len(crawler.screens))
    presentation = composer.compose(crawler.screens)
    Logger.rewrite('Working: saving presentation')
    presentation.save('dist/game.pptx')
    Logger.write('Done: presentation saved')

LEVELS = [
    [
        '🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱',
        '🧱💎⬛⬛⬛🧱⬛🤴⬛⬛🧱⬛⬛⬛⬛🧱',
        '🧱⬛🧱🧱⬛🧱🧱🧱🧱🐲🧱⬛🧱🧱⬛🧱',
        '🧱⬛⬛🧱⬛⬛🧱⬛🧱⬛⬛⬛🧱⬛⬛🧱',
        '🧱🧱🧱🧱🧱⬛🧱⬛⬛⬛🧱⬛🧱⬛🧱🧱',
        '🧱🗝️⬛⬛🧱⬛🧱🧱🔒🧱🧱🧱🧱⬛🧱🧱',
        '🧱🧱🧱⬛🧱⬛⬛⬛⬛🧱⬛⬛🧱⬛⬛🧱',
        '🧱💎🧱⬛🧱🧱🧱🧱⬛🧱⬛🧱🧱🧱⬛🧱',
        '🧱⬛🧱⬛⬛⬛⬛🧱⬛🧱⬛⬛⬛🧱⬛🧱',
        '🧱⬛🧱🧱⬛🧱⬛🧱⬛🧱🧱🧱⬛🧱⬛🧱',
        '🧱⬛⬛⬛⬛🧱⬛⬛🧙⬛⬛⬛⬛🧱💎🧱',
        '🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱',
    ],
]

ASSETS = {
    f'Image.Button[{Button.CLOSE}]': 'asset/menu/close.png',
    f'Image.Button[{Button.DOWN}]': 'asset/move/down.png',
    f'Image.Button[{Button.LEFT}]': 'asset/move/left.png',
    f'Image.Button[{Button.PLAY}]': 'asset/menu/play.png',
    f'Image.Button[{Button.RIGHT}]': 'asset/move/right.png',
    f'Image.Button[{Button.UP}]': 'asset/move/up.png',
    f'Image.Item[{Cell.GEM}].Having': 'asset/item/gem_1.png',
    f'Image.Item[{Cell.GEM}].Missing': 'asset/item/gem_0.png',
    f'Image.Item[{Cell.KEY}].Having': 'asset/item/key_1.png',
    f'Image.Maze[{Cell.LOCK}]': 'asset/maze/door_0.png',
    f'Image.Maze[{Cell.DOOR}]': 'asset/maze/door_1.png',
    f'Image.Maze[{Cell.DRAGON}]': 'asset/character/dragon.png',
    f'Image.Maze[{Cell.GEM}]': 'asset/maze/gem.png',
    f'Image.Maze[{Cell.KEY}]': 'asset/maze/key.png',
    f'Image.Maze[{Cell.PRINCESS}]': 'asset/character/princess.png',
    f'Image.Maze[{Cell.SPACE}]': 'asset/maze/space.png',
    f'Image.Maze[{Cell.WALL}]': 'asset/maze/wall_0.png',
    f'Image.Maze[{Cell.WIZARD}]': 'asset/character/wizard.png',
    f'Image.Menu[{"BACKGROUND"}]': 'asset/maze/space.png',
    f'Image.Menu[{"CREDITS"}]': 'asset/menu/credits.png',
    f'Image.Menu[{"DIALOG"}]': 'asset/menu/dialog.png',
    f'Image.Menu[{"LOGO"}]': 'asset/menu/logo.png',
    f'Message[{Message.DOOR_LOCKED}]': 'The door is locked. Find the key!',
    f'Message[{Message.DRAGON_BLOCK}]': 'You want me to move? No way. Maybe for 3 diamonds though!',
    f'Message[{Message.DRAGON_BRIBE}]': 'Niiiice, 3 diamonds. Yummy! You may proceed.',
    f'Message[{Message.PRINCESS_MESSAGE}]': 'You want to save me? Maybe for 3 diamonds.',
    f'Music[{Music.THEME}]': 'asset/menu/intro.mp3',
    f'Sound[{Sound.BUTTON_HIT}]': 'asset/menu/button.wav',
    f'Sound[{Sound.DOOR_HIT}]': 'asset/maze/door.wav',
    f'Sound[{Sound.DOOR_UNLOCK}]': 'asset/maze/unlock.wav',
    f'Sound[{Sound.DRAGON_ROAR}]': 'asset/character/roar.wav',
    f'Sound[{Sound.FLOOR_WALK}]': 'asset/move/walk.wav',
    f'Sound[{Sound.GEM_PICKUP}]': 'asset/item/gem.wav',
    f'Sound[{Sound.KEY_PICKUP}]': 'asset/item/key.wav',
    f'Sound[{Sound.PRINCESS_LAUGH}]': 'asset/character/laugh.wav',
    f'Sound[{Sound.WALL_HIT}]': 'asset/maze/wall.wav',
}

if __name__ == '__main__':
    main()
