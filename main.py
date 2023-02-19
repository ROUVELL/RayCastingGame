import pygame as pg

from world import World
from player import Player
from renderer import Renderer
from ray_casting import RayCasting
from sprite_object import SpriteObject
from settings import *


class Game:
    def __init__(self):
        pg.init()
        pg.event.clear()
        pg.mouse.set_visible(False)
        pg.event.set_blocked(None)
        pg.event.set_allowed([pg.KEYUP, pg.QUIT])
        self.sc = pg.display.set_mode(SCREEN)
        self.clock = pg.time.Clock()
        self.dt = 0.0
        self.start()

    def start(self):
        self.world = World(self)
        self.player = Player(self)
        self.renderer = Renderer(self)
        self.ray_casting = RayCasting(self)
        self.static_sprite = SpriteObject(self)
        self.static_sprite2 = SpriteObject(self, 'resources/sprites/static/anime_girl_2.png', pos=(9.5, 6.7), shift=.48)

    def update(self):
        self.player.update()
        self.ray_casting.update()
        self.static_sprite.update()
        self.static_sprite2.update()

    def draw(self):
        # self.sc.fill('black')
        # self.world.draw()
        # self.player.draw()
        self.renderer.draw()

    def run(self):
        while True:
            self.dt = self.clock.tick(0)
            [exit() for event in pg.event.get() if event.type == pg.QUIT or event.key == pg.K_ESCAPE]
            self.update()
            self.draw()
            pg.display.set_caption(f'{self.clock.get_fps(): .1f}')
            pg.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()