import pgzrun
import random

WIDTH = 800
HEIGHT = 600

ball = Actor('ball')
ball.pos = (WIDTH/2, ball.height)
ball.speed_x = random.choice([-2,-1,1,2])
ball.speed_y = random.choice([1,2])

bat = Actor('bat')
bat.pos = (WIDTH/2, HEIGHT - (bat.height*2))

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
    bat.draw()

def update():
    if_on_edge_bounce(ball)
    ball.x += ball.speed_x
    ball.y += ball.speed_y
    if ball.colliderect(bat):
        # bounce up
        ball.speed_y = -abs(ball.speed_y)

def on_mouse_move(pos):
    bat.pos = pos
    
pgzrun.go() 
