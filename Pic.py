import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((1800, 800))
line(screen, (175,238,238), (1800,200), (0,200), 400)
line(screen, (152,251,152), (1800,600), (0,600), 400)
x, y = 50, 0
#pygame.quit()

#мороженное
def ice(x, y, z=1, da=0):
    if da == 0:
        polygon(screen,(255,255,1), [(200+x,420+y), (200+x,420-40*z+y), (200-40*z+x, 420-40*z+y)])
        circle(screen,(255,1,1), (200-10*z+x,420-50*z+y), 15*z)
        circle(screen,(255,1,186), (200-30*z+x,420-40*z+y), 15*z)
        circle(screen,(255,175,1), (200-20*z+x,420-60*z+y), 15*z)
    else:
        polygon(screen,(255,255,1), [(200+x,420+y), (200+x,420-60*z+y), (200+40*z+x, 420-40*z+y)])
        circle(screen,(255,1,1), (200+10*z+x,420-50*z+y), 15*z)
        circle(screen,(255,1,186), (200+30*z+x,420-40*z+y), 15*z)
        circle(screen,(255,175,1), (200+20*z+x,420-60*z+y), 15*z)
        
#шарик
def lov(x, y, z):
    line(screen,(0,0,0), (680+x, 340+y),(680+20*z+x,340-140*z+y), 1*z)
    polygon(screen,(255,1,1), [(680+20*z+x,340-140*z+y), (680+60*z+x,340-170*z+y), (680+10*z+x,340-180*z+y)])
    circle(screen,(255,1,1), (680+20*z+x,340-190*z+y), 20*z)
    circle(screen,(255,1,1), (680+50*z+x,340-180*z+y), 20*z)


#мальчик
def man(x, y, z, da):
    if da == 0:
        da = 1
    else:
        da = -1
    ellipse(screen,(80, 80, 80), (300+50*z*(da - 1)+x,250+y, 100*z, 275*z))
    circle(screen,(245,245,220), (300+50*z*da+x,250-30*z+y), 40*z)
    line(screen,(0,0,0), (300+20*z*da+x,250+30*z+y), (300-100*z*da+x, 250+170*z+y),1*z)
    line(screen,(0,0,0), (300+80*z*da+x,250+30*z+y), (300+200*z*da+x, 250+170*z+y),1*z)

    line(screen,(0,0,0), (300+20*z*da+x,250+240*z+y), (300-50*z*da+x, 250+400*z+y),1*z)
    line(screen,(0,0,0), (300-50*z*da+x,250+400*z+y), (300-70*z*da+x, 250+y+400*z),1*z)
    line(screen,(0,0,0), (300+80*z*da+x,250+240*z+y), (300+150*z*da+x, 250+y+400*z),1*z)
    line(screen,(0,0,0), (300+150*z*da+x,250+400*z+y), (300+170*z*da+x, 250+y+400*z),1*z)


def girle(x, y, z, da):
    if da == 0:
        da = 1
    else:
        da = -1
    polygon(screen,(255,192,203), [(600+x,250+y), (600+60*z*da+x,250+275*z+y), (600-60*z*da+x,250+275*z+y)])
    circle(screen,(245,245,220), (600+x,250-30*z+y), 40*z)
    line(screen,(0,0,0), (600+5*z*da+x,250+30*z+y), (600+55*z*da+x, 250+120*z+y),1*z)
    line(screen,(0,0,0), (600+55*z*da+x, 250+120*z+y),(600+90*z*da+x,250+30*z+y), 1*z)
    line(screen,(0,0,0), (600-5*z*da+x,250+30*z+y), (600-100*z*da+x, 250+170*z+y),1*z)
    f = 250+400*z+y
    line(screen,(0,0,0), (600-20*z*da+x,250+275*z+y), (600-70*z*da+x, f),1*z)
    line(screen,(0,0,0), (600-70*z*da+x,250+400*z+y), (600-90*z*da+x, f),1*z)
    line(screen,(0,0,0), (600+20*z*da+x,250+275*z+y), (600+70*z*da+x, f),1*z)
    line(screen,(0,0,0), (600+70*z*da+x,250+400*z+y), (600+90*z*da+x, f),1*z)

z = 1
man(x, y, z, 0)
girle(x, y, z, 0)
lov(x, y, z)
ice(x, y, z, 0)
#вторая пара
q = z*200
man(x+600+q, y, z, -1)
girle(x+q, y, z, -1)
ice(x+800+q, y, z, -1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
