import pygame as pg
from math import sin, cos, tau

from settings import *


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = 0
        self.rel = 0

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)

    def check_wall(self, x, y):
        return (x, y) not in self.game.world.map

    def check_wall_collision(self, dx, dy):
        scale = PLAYER_SIZE / self.game.dt
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def movement(self):
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.dt
        speed_sin = speed * sin(self.angle)
        speed_cos = speed * cos(self.angle)

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.check_wall_collision(dx, dy)

    def mouse_control(self):
        self.rel = pg.mouse.get_rel()[0]
        mx, my = pg.mouse.get_pos()
        if not MOUSE_RECT.collidepoint(mx, my):
            pg.mouse.set_pos(CENTER)
            pg.mouse.get_rel()
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.dt
        self.angle %= tau

    def update(self):
        self.movement()
        self.mouse_control()

    def draw(self):
        pg.draw.line(self.game.sc, 'green', (self.x * 100, self.y * 100),
                     (self.x * 100 + WIDTH * cos(self.angle),
                      self.y * 100 + WIDTH * sin(self.angle)))
        pg.draw.circle(self.game.sc, 'green', (self.x * 100, self.y * 100), 10)
