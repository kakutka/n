import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((1200, 600))
line(screen, (175,238,238), (1800,200), (0,200), 400)
line(screen, (152,251,152), (1800,600), (0,600), 400)
x, y = 50, 0
#pygame.quit()


#x, y - положение; z - размер; da - отражение, при 0 нормальное, при не 0 обратное
#создаёт мороженное, меняет его положение, размер и симметрию
def ice(x, y, z=1, da=0):
    if da == 0:
        polygon(screen,(255,255,1), [(200+x,420+y), (200+x,420-int(40*z)+y), (200-int(40*z)+x, 420-int(40*z)+y)])
        circle(screen,(255,1,1), (200-int(10*z)+x,420-int(50*z)+y), int(15*z))
        circle(screen,(255,1,186), (200-int(30*z)+x,420-int(40*z)+y), int(15*z))
        circle(screen,(255,175,1), (200-int(20*z)+x,420-int(60*z)+y), int(15*z))
    else:
        polygon(screen,(255,255,1), [(200+x,420+y), (200+x,420-int(60*z)+y), (200+int(40*z)+x, 420-int(40*z)+y)])
        circle(screen,(255,1,1), (200+int(10*z)+x,420-int(50*z)+y), int(15*z))
        circle(screen,(255,1,186), (200+int(30*z)+x,420-int(40*z)+y), int(15*z))
        circle(screen,(255,175,1), (200+int(20*z)+x,420-int(60*z)+y), int(15*z))

#создаёт шарик, меняет его положение, размер
def lov(x, y, z):
    line(screen,(0,0,0), (680+x, 340+y),(680+int(20*z)+x,340-int(140*z)+y), int(1*z)+1)
    polygon(screen,(255,1,1), [(680+int(20*z)+x,340-int(140*z)+y), (680+int(60*z)+x,340-int(170*z)+y), (680+int(10*z)+x,340-int(180*z)+y)])
    circle(screen,(255,1,1), (680+int(20*z)+x,340-int(190*z)+y), int(20*z))
    circle(screen,(255,1,1), (680+int(50*z)+x,340-int(180*z)+y), int(20*z))


#создаёт мальчика, меняет его положение, размер и симметрию
def man(x, y, z, da):
    if da == 0:
        da = 1
    else:
        da = -1
    ellipse(screen,(80, 80, 80), (300+int(50*z)*(da - 1)+x,250+y, int(100*z), int(275*z)))
    circle(screen,(245,245,220), (300+int(50*z)*da+x,250-int(30*z)+y), int(40*z))
    line(screen,(0,0,0), (300+int(20*z)*da+x,250+int(30*z)+y), (300-int(100*z)*da+x, 250+int(170*z)+y),int(1*z)+1)
    line(screen,(0,0,0), (300+int(80*z)*da+x,250+int(30*z)+y), (300+int(200*z)*da+x, 250+int(170*z)+y),int(1*z)+1)

    line(screen,(0,0,0), (300+int(20*z)*da+x,250+int(240*z)+y), (300-int(50*z)*da+x, 250+int(400*z)+y),int(1*z)+1)
    line(screen,(0,0,0), (300-int(50*z)*da+x,250+int(400*z)+y), (300-int(70*z)*da+x, 250+y+int(400*z)),int(1*z)+1)
    line(screen,(0,0,0), (300+int(80*z)*da+x,250+int(240*z)+y), (300+int(150*z)*da+x, 250+y+int(400*z)),int(1*z)+1)
    line(screen,(0,0,0), (300+int(150*z)*da+x,250+int(400*z)+y), (300+int(170*z)*da+x, 250+y+int(400*z)),int(1*z)+1)

#создаёт девочку, меняет её положение, размер и симметрию
def girle(x, y, z, da):
    if da == 0:
        da = 1
    else:
        da = -1
    polygon(screen,(255,192,203), [(600+x,250+y), (600+int(60*z)*da+x,250+int(275*z)+y), (600-int(60*z)*da+x,250+int(275*z)+y)])
    circle(screen,(245,245,220), (600+x,250-int(30*z)+y), int(40*z))
    line(screen,(0,0,0), (600+int(5*z)*da+x,250+int(30*z)+y), (600+int(55*z)*da+x, 250+int(120*z)+y),int(1*z)+1)
    line(screen,(0,0,0), (600+int(55*z)*da+x, 250+int(120*z)+y),(600+int(90*z)*da+x,250+int(30*z)+y), int(1*z)+1)
    line(screen,(0,0,0), (600-int(5*z)*da+x,250+int(30*z)+y), (600-int(100*z)*da+x, 250+int(170*z)+y),int(1*z)+1)
    f = 250+int(400*z)+y
    line(screen,(0,0,0), (600-int(20*z)*da+x,250+int(275*z)+y), (600-int(70*z)*da+x, f),int(1*z)+1)
    line(screen,(0,0,0), (600-int(70*z)*da+x,250+int(400*z)+y), (600-int(90*z)*da+x, f),int(1*z)+1)
    line(screen,(0,0,0), (600+int(20*z)*da+x,250+int(275*z)+y), (600+int(70*z)*da+x, f),int(1*z)+1)
    line(screen,(0,0,0), (600+int(70*z)*da+x,250+int(400*z)+y), (600+int(90*z)*da+x, f),int(1*z)+1)

z = 1


#создает целую картинку из объектов, которую можно перемещать, увеличивать и уменьшать
def fix(x, y, z):
    #вызов функций
    man(x, y, z, 0)
    girle(x + int(310*(z-1)), y, z, 0)
    lov(x + int(380*(z-1)), y+int(100*(z-1)), z)
    ice(x+100-int(100*z), y-170+int(170*z), z, 0)
    #вторая пара
    q = int(z*200)
    man(x+int(600*z)+q, y, z, -1)
    girle(x+q+int(290*(z-1)), y, z, -1)
    ice(x+int(800*z)+100-int(100*z)+q, y-170+int(170*z), z, -1)
    
fix(x, y, 1.5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
