# Copyright 2019, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""Version 1 of classic Asteroids game - many rocks"""

import pgzrun
from helpers import *
import random, math

WIDTH = 800
HEIGHT = 600
NUM_ROCKS = 5
KEYS = {}

ship = Actor('ship')
ship.pos = (WIDTH/2, HEIGHT/2)
ship.speed = 0

def new_rock():
    rock = Actor('rock')
    rock.pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
    rock.speed_x = random.random() - 0.5
    rock.speed_y = random.random() - 0.5
    rock.rotate_direction = (random.random() - 0.5)*0.2
    return rock

rocks = []
for i in range(NUM_ROCKS):
    rocks.append(new_rock())
    
def draw():
    screen.clear()
    ship.draw()
    for rock in rocks:
        rock.draw()

def update():
    for rock in rocks:
        if_on_edge_wrap(rock, WIDTH, HEIGHT)
        rock.x += rock.speed_x
        rock.y += rock.speed_y
        rock.angle += rock.rotate_direction
        
    if keys.LEFT in KEYS:
        ship.angle += 2
    if keys.RIGHT in KEYS:
        ship.angle -= 2
    if keys.UP in KEYS:
        ship.speed += .2

    if_on_edge_wrap(ship, WIDTH, HEIGHT)
    ship.x += math.cos(math.radians(270 - ship.angle)) * ship.speed
    ship.y += math.sin(math.radians(270 - ship.angle)) * ship.speed
        
def on_key_down(key):
    KEYS[key] = True

def on_key_up(key):
    if key in KEYS:
        del(KEYS[key])
        
pgzrun.go()
