import pygame as pg
from math import hypot, atan2, cos, tau, pi

from settings import *


class SpriteObject:
    def __init__(self, game, path='resources/sprites/static/anime_girl_1.png',
                 pos=(9.5, 6.3), scale=0.7, shift=0.44):
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.scale = scale
        self.shift = shift
        self.img = pg.image.load(path).convert_alpha()
        self.IMG_WIDTH = self.img.get_width()
        self.H_IMG_WIDTH = self.IMG_WIDTH // 2
        self.IMG_RATIO = self.IMG_WIDTH / self.img.get_height()

    def get_sprite_projection(self, screen_x, norm_dist):
        proj = SCREEN_DIST / norm_dist * self.scale
        proj_w, proj_h = proj * self.IMG_RATIO, proj

        img = pg.transform.scale(self.img, (proj_w, proj_h))

        h_sprite_width = proj_w // 2
        height_shift = proj_h * self.shift
        pos = (screen_x - h_sprite_width, H_HEIGHT - proj_h // 2 + height_shift)

        self.game.ray_casting.to_render.append((norm_dist, img, pos))

    def get_sprite(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        theta = atan2(dy, dx)
        delta = theta - self.player.angle
        if (dx > 0 and self.player.angle > pi) or (dx < 0 and dy < 0):
            delta += tau

        delta_rays = delta / DELTA_ANGLE
        screen_x = (H_NUM_RAYS + delta_rays) * SCALE

        dist = hypot(dx, dy)
        norm_dist = dist * cos(delta)
        if -self.H_IMG_WIDTH < screen_x < (WIDTH + self.H_IMG_WIDTH) and norm_dist > .5:
            self.get_sprite_projection(screen_x, norm_dist)

    def update(self):
        self.get_sprite()