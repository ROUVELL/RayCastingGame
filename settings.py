from pygame import Rect
from math import pi, tan

# screen
SCREEN = WIDTH, HEIGHT = 1600, 900
CENTER = H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2

# player
PLAYER_POS = (1.5, 5)
PLAYER_SPEED = .003
PLAYER_SIZE = 60

# ray casting
FOV = pi / 3
H_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
H_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 25

SCREEN_DIST = H_WIDTH / tan(H_FOV)
SCALE = WIDTH // NUM_RAYS

# control
MOUSE_RECT = Rect(200, 200, WIDTH - 400, HEIGHT - 400)  # left, top, width, height
MOUSE_SENSITIVITY = .0001

TEXTURE_SIZE = 512
H_TEXTURE_SIZE = TEXTURE_SIZE // 2

# colors
SKY = (135, 206, 235)
FLOOR = (35, 35, 35)