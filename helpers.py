# Copyright 2019, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""Helper functions for games examples"""

import math


def if_on_edge_bounce(sprite, width, height):
    if sprite.left <= 0:
        sprite.speed_x = abs(sprite.speed_x)
    elif sprite.right >= width:
        sprite.speed_x = -abs(sprite.speed_x)
    if sprite.top <= 0:
        sprite.speed_y = abs(sprite.speed_y)
    elif sprite.bottom >= height:
        sprite.speed_y = -abs(sprite.speed_y)        


def if_on_edge_wrap(sprite, width, height):
    if sprite.right <= 0:
        sprite.left = width
    elif sprite.left >= width:
        sprite.right = 0
    if sprite.bottom <= 0:
        sprite.top = height
    elif sprite.top >= height:
        sprite.bottom = 0
        

def move_forward(sprite, distance):
    """Move sprite in direction of angle by distance.

    We assuming sprite is drawn with front at top of image.
    """
    
    sprite.x += math.cos(math.radians(270 - sprite.angle)) * distance
    sprite.y += math.sin(math.radians(270 - sprite.angle)) * distance
