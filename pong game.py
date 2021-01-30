import pygame
import sys



screen_width=800
screen_height=600
black=(0,0,0)
blue=(34,78,90)
fps=60
ballradius=24
ballx=ballradius
bally=ballradius
speed=[2,2]


pygame.init()

def animate_ball():
    global ballx,bally
    ballx+=speed[0]
    bally+=speed[1]


def check_boundary():
    if ballx<screen_width or ballx<0:
        speed[0]*=-1
    if bally<screen_height or bally<0:
        speed[1]*=-1

screen=pygame.display.set_mode([screen_width,screen_height])
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event==pygame.QUIT:
            sys.exit()
    screen.fill(black)
    pygame.draw.circle(screen,blue,[ballx,bally],ballradius)
    animate_ball()
    pygame.display.update()
    clock.tick(fps)
