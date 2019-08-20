# Copyright 2019, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""Version 0 of classic Pong game - just a ball"""

import pgzrun
import random

WIDTH = 800
HEIGHT = 600

ball = Actor('ball')
ball.pos = (WIDTH/2, ball.height)
ball.speed_x = random.choice([-2,-1,1,2])
ball.speed_y = random.choice([1,2])

def if_on_edge_bounce(sprite):
    if sprite.left <= 0:
        sprite.speed_x = abs(sprite.speed_x)
    elif sprite.right >= WIDTH:
        sprite.speed_x = -abs(sprite.speed_x)
    if sprite.top <= 0:
        sprite.speed_y = abs(sprite.speed_y)
    elif sprite.bottom >= HEIGHT:
        sprite.speed_y = -abs(sprite.speed_y)        

def draw():
    screen.clear()
    ball.draw()

def update():
    if_on_edge_bounce(ball)
    ball.x += ball.speed_x
    ball.y += ball.speed_y
    
pgzrun.go() 
