# Copyright 2019, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""Version 0 of classic Asteroids game - just a rock"""

import pgzrun
import random

WIDTH = 800
HEIGHT = 600

rock = Actor('rock')
rock.pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
rock.speed_x = random.random() - 0.5
rock.speed_y = random.random() - 0.5
rock.rotate_direction = random.random() - 0.5

def draw():
    screen.clear()
    rock.draw()

def update():
    rock.x += rock.speed_x
    rock.y += rock.speed_y
    rock.angle += rock.rotate_direction

pgzrun.go()
