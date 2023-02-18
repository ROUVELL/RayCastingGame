import pygame as pg

from settings import *


class Game:
    def __init__(self):
        pg.init()
        pg.event.clear()
        pg.event.set_blocked(None)
        pg.event.set_allowed([pg.KEYUP, pg.QUIT])
        self.sc = pg.display.set_mode(SCREEN)
        self.clock = pg.time.Clock()

    def run(self):
        while True:
            self.clock.tick(60)
            [exit() for event in pg.event.get() if event.type == pg.QUIT or event.key == pg.K_ESCAPE]
            # update
            # draw
            pg.display.set_caption(f'{self.clock.get_fps(): .1f}')
            pg.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()