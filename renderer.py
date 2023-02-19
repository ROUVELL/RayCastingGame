import pygame as pg

from settings import *


class Renderer:
    def __init__(self, game):
        self.game = game
        self.sc = game.sc
        #########
        self.wall_textures = {1: self.get_texture('resources/textures/1.png'),
                              2: self.get_texture('resources/textures/2.png'),
                              3: self.get_texture('resources/textures/3.png'),
                              4: self.get_texture('resources/textures/4.png')}
        self.sky = self.get_texture('resources/textures/sky.png', (WIDTH, H_HEIGHT))
        self.sky_offset = 0

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def bg(self):
        self.sky_offset = (self.sky_offset + 4 * self.game.player.rel) % WIDTH
        self.sc.blit(self.sky, (-self.sky_offset, 0))
        self.sc.blit(self.sky, (-self.sky_offset + WIDTH, 0))
        pg.draw.rect(self.sc, FLOOR, (0, H_HEIGHT, WIDTH, H_HEIGHT))

    def game_objs(self):
        objs = sorted(self.game.ray_casting.to_render, key=lambda t: t[0], reverse=True)
        for depth, img, pos in objs:
            self.sc.blit(img, pos)

    def draw(self):
        self.bg()
        self.game_objs()



