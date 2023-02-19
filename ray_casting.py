import pygame as pg
from math import sin, cos

from settings import *


class RayCasting:
    def __init__(self, game):
        self.game = game
        self.result = []
        self.to_render = []
        self.textures = self.game.renderer.wall_textures

    def get_objs_to_render(self):
        self.to_render.clear()
        for ray, value in enumerate(self.result):
            depth, proj_height, texture, offset = value
            if proj_height < HEIGHT:
                wall_column = self.textures[texture].subsurface(
                    offset * (TEXTURE_SIZE - SCALE), 0, SCALE, TEXTURE_SIZE
                )
                wall_column = pg.transform.scale(wall_column, (SCALE, proj_height))
                wall_pos = (ray * SCALE, H_HEIGHT - proj_height // 2)
            else:
                texture_height = TEXTURE_SIZE * HEIGHT / proj_height
                wall_column = self.textures[texture].subsurface(
                    offset * (TEXTURE_SIZE - SCALE), H_TEXTURE_SIZE - texture_height // 2,
                    SCALE, texture_height
                )
                wall_column = pg.transform.scale(wall_column, (SCALE, HEIGHT))
                wall_pos = (ray * SCALE, 0)

            self.to_render.append((depth, wall_column, wall_pos))

    def ray_cast(self):
        self.result.clear()
        px, py = self.game.player.pos
        map_x, map_y = self.game.player.map_pos

        vert_texture, hor_texture = 1, 1
        ray_angle = self.game.player.angle - H_FOV + .0001
        for ray in range(NUM_RAYS):
            sin_a = sin(ray_angle)
            cos_a = cos(ray_angle)

            # horizontals
            y_hor, dy = (map_y + 1, 1) if sin_a > 0 else (map_y - 1e-6, -1)
            hor_depth = (y_hor - py) / sin_a
            x_hor = px + hor_depth * cos_a
            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for _ in range(MAX_DEPTH):
                hor_tile = int(x_hor), int(y_hor)
                if hor_tile in self.game.world.map:
                    hor_texture = self.game.world.map[hor_tile]
                    break
                x_hor += dx
                y_hor += dy
                hor_depth += delta_depth

            # verticals
            x_vert, dx = (map_x + 1, 1) if cos_a > 0 else (map_x - 1e-6, -1)
            vert_depth = (x_vert - px) / cos_a
            y_vert = py + vert_depth * sin_a
            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for _ in range(MAX_DEPTH):
                vert_tile = int(x_vert), int(y_vert)
                if vert_tile in self.game.world.map:
                    vert_texture = self.game.world.map[vert_tile]
                    break
                x_vert += dx
                y_vert += dy
                vert_depth += delta_depth

            # depth, texture, offset
            if vert_depth < hor_depth:
                depth, texture = vert_depth, vert_texture
                y_vert %= 1
                offset = y_vert if cos_a > 0 else 1 - y_vert
            else:
                depth, texture = hor_depth, hor_texture
                x_hor %= 1
                offset = x_hor if sin_a > 0 else 1 - x_hor


            depth *= cos(self.game.player.angle - ray_angle)

            # projection
            proj_height = SCREEN_DIST / (depth + .0001)

            self.result.append((depth, proj_height, texture, offset))

            ray_angle += DELTA_ANGLE

    def update(self):
        self.ray_cast()
        self.get_objs_to_render()
