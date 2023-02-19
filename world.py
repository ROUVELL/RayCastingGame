import pygame as pg

from settings import *

_ = False
level = [
    [_, 1, 1, 1, 3, 1, 1, 1, 1, _, _, _, _, _, _, _, _, 3, 3, 1, 1, 1, 1, _],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2],
    [1, _, _, 3, 1, 1, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 4],
    [1, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2],
    [3, _, _, _, _, _, 3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2],
    [1, _, _, 1, 3, 1, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 4],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 2],
    [_, 3, 1, 1, 1, 1, 1, 1, 3, _, _, _, _, _, _, _, _, 1, 1, 1, 3, 1, 1, _]
]


class World:
    def __init__(self, game):
        self.game = game
        self.map = self.load_map('resources/levels/1.txt')

    @staticmethod
    def load_map(path):
        map_ = {}
        with open(path, encoding='utf-8') as level:
            for y, row in enumerate(level.readlines()):
                for x, value in enumerate(row[:-1]):
                    if int(value):
                        map_[(x, y)] = int(value)
        return map_

    @staticmethod
    def get_map(level):
        map_ = {}
        for y, row in enumerate(level):
            for x, value in enumerate(row):
                if value:
                    map_[(x, y)] = value
        return map_

    def draw(self):
        [pg.draw.rect(self.game.sc, 'grey', (x * 100, y * 100, 100, 100), 1)
         for x, y in self.map]

