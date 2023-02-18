import pygame as pg

from settings import SCREEN


class Game:
    def __init__(self):
        pg.init()
        self.sc = pg.display.set_mode(SCREEN)
        self.clock = pg.time.Clock()

    def run(self):
        while True:
            self.clock.tick(60)
            [exit() for event in pg.event.get() if event.type == pg.KEYUP and event.key == pg.K_ESCAPE]

            pg.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()