# Copyright 2019, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""Version 1 of classic Pong game, with a bat and ball
but no bricks.
"""

import pgzrun
from helpers import *
import random

WIDTH = 800
HEIGHT = 600

ball = Actor('ball')
ball.pos = (WIDTH/2, ball.height)
ball.speed_x = random.choice([-2,-1,1,2])
ball.speed_y = random.choice([1,2])

bat = Actor('bat')
bat.pos = (WIDTH/2, HEIGHT - (bat.height*2))

def draw():
    screen.clear()
    ball.draw()
    bat.draw()

def update():
    if_on_edge_bounce(ball, WIDTH, HEIGHT)
    ball.x += ball.speed_x
    ball.y += ball.speed_y
    if ball.colliderect(bat):
        # bounce up
        ball.speed_y = -abs(ball.speed_y)

def on_mouse_move(pos):
    bat.pos = pos
    
pgzrun.go() 
