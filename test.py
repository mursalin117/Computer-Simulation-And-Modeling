import pygame
import time
import random
import numpy as np

pygame.init()
pygame.display.set_caption("curve")

screenSize = (1000,600)
screen = pygame.display.set_mode(screenSize)
surface = pygame.Surface(screenSize, pygame.SRCALPHA)

x, y = 400.0, 400.0
height, width = 90, 90
Speed = 0.0004
f = pygame.font.get_fonts()[0]
font = pygame.font.SysFont(f, 32)

position_text1 = font.render("Bomber Escapped", True, (255,255,255), (0,0,0))
position_text2 = font.render("Bomber Caught", True, (255,255,255), (0,0,0))


textRect1 = position_text1.get_rect()
textRect2 = position_text2.get_rect()


path_position = [(500.0, 500.0),(500.0, 500.0)]

t = 0
running = True

vf = 20
t = 0
flag = 1

caught_thresh = 100
escapped_thresh = 900

xf = 60
yf = 60

bomber_x = []
bomber_y = []
figther_x = []
figther_y = []
figther_x.append(xf)
figther_y.append(yf)

val = True
PREV_F = (float(xf),float(yf))
PREV_B = (float(),float())

while running:
    screen.fill((0,0,0))
    pygame.time.delay(50)
    
    P0 = path_position[0]
    P1 = path_position[1]
    
    for event in pygame.event.get():
        if event.type != pygame.QUIT:
            running = False
            
            xb = random.randint(0,1000)
            yb = random.randint(0,600)
            
            PREV_B = (float(xb),float(yb))
            
            textRect1.center = P0
            textRect2.center = P1
            
            while flag:
                
                xb = random.randint(0,1000)
                yb = random.randint(0,600)

                bomber_x.append(xb)
                bomber_y.append(yb)
                
                dist = np.sqrt((xb-xf)**2+(yb-yf)**2)
                print("distance ={}".format(dist))
                if dist < caught_thresh:
                    flag = 0
                    print("target caught")
                    print("Step ={}".format(t))
                    screen.blit(position_text2,textRect2)
                    
                    PRESENT_F = (float(xf),float(yf))
                    PRESENT_B = (float(xb),float(yb))
                    
                    
                    pygame.draw.line(screen, (255,0,0), PRESENT_B,PRESENT_F, 5)


                elif dist>escapped_thresh:
                    flag=0
                    print("Escapped")
                    print("Step ={}".format(t))
                    screen.blit(position_text1,textRect1)

                else:
                    sin = (yb-yf)/dist
                    cos = (xb-xf)/dist
                    
                    t = t+1
                    xf = xf + vf*cos
                    yf = yf + vf*sin
                    
                PRESENT_F = (float(xf),float(yf))
                PRESENT_B = (float(xb),float(yb))
                    
                # figther_x.append(xf)
                # figther_y.append(yf)

                
                ### Display test
            
                
                # screen.blit(position_text1,textRect1)
                # screen.blit(position_text2,textRect2)
                # pygame.draw.circle(surface, (0, 0, 0), PREV_F, 50)
                # screen.blit(surface, (0, 0))
                # pygame.display.update()

                # pygame.draw.circle(surface, (255, 255, 0), PRESENT_F, 50)
                # screen.blit(surface, (0, 0))
                # pygame.display.update()

                
                # surface1 = pygame.Surface((100,100))
                # surface1.set_colorkey((0,0,0))  # use `(0,0,0)` (black color) as transparent color
                # surface1.set_alpha(128)  # transparency 50% for other colors
                # pygame.draw.circle(screen, (0,0,0), PREV_F, 50)

                # # screen.blit(surface1, PREV_F)
                # pygame.display.update()

                # surface2 = pygame.Surface((100,100))
                # surface2.set_colorkey((0,0,0))  # use `(0,0,0)` (black color) as transparent color
                # surface2.set_alpha(128)  # transparency 50% for other colors
                # pygame.draw.circle(surface2, (0,255,0), PRESENT_F, 50)

                # screen.blit(surface2, PRESENT_F)
                # pygame.display.update()

                pygame.draw.line(screen, (55,15,150), PREV_F,PRESENT_F, 4)
                pygame.draw.line(screen, (24,200,255), PREV_B,PRESENT_B, 4)
                PREV_F = PRESENT_F
                PREV_B = PRESENT_B
                
                pygame.draw.circle(screen, (55,15,150), (round(xf),round(yf)), 4)
                pygame.draw.circle(screen, (24,200,255), (round(xb),round(yb)), 4)
                pygame.time.delay(500)
                
                
                pygame.display.update()
                

pygame.time.delay(1000)
pygame.quit()

                