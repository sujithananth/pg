#ellipes orbitS
import pygame
import sys
import math



screen_width=800
screen_height=600
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
white=(255,255,255)
centerx=screen_width//2
centery=screen_height//2
sunradius=40
ballradius=20
orbitxradius=350
orbityradius=200


pygame.init()
def orbits(x,y):
    pygame.draw.ellipse(screen,white,[x,y,700,400],1)
def planets(degree,color,):
    x=int(math.cos(degree*math.pi/180)*orbitxradius)+centerx
    y=int(math.sin(degree*math.pi/180)*orbityradius)+centery
    pygame.draw.circle(screen,color,[x,y],ballradius)


screen=pygame.display.set_mode([screen_width,screen_height])
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event==pygame.QUIT:
            sys.exit()
    for degree in range(0,360):
         screen.fill(black)
         pygame.draw.circle(screen,red,[centerx,centery],sunradius)
         planets(degree,blue)
         orbits(50,100)
         pygame.display.update()
         clock.tick(60)
