import pygame
import random
import time
#Reguired libraries


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Matopeli')

x = 200 #beginning point of snake x
y = 200 #beginning point of snake y
BLACK = 0,0,0 #Colour
WHITE = 255,255,255 #Colour
RED = 240,0,100 #Colour
width = 10 # Size of snake
height = 10 # Size of snake
vel = 10  # In what speed rectangle is moving
UP = False  # As beginning all buttons ore False
DOWN = False # As beginning all buttons ore False
LEFT = False # As beginning all buttons ore False
RIGHT = False # As beginning all buttons ore False
x2 = random.randrange(10,490,10) # Random integer for new 'Apple'
y2 = random.randrange(10,450,10) # Random integer for new 'Apple'
points = [] #Points
xpoint = [] #Place of body
ypoint = [] #Place of body

def text_objects(text, font): #Text
    TextSurf = font.render(text, True, WHITE)
    return TextSurf, TextSurf.get_rect()

def message_display(text):
    text_l = pygame.font.Font('freesansbold.ttf', 20) #textFONT
    TextSurf, TextReact = text_objects(text, text_l)
    TextReact.center = (85, 460)
    screen.blit(TextSurf, TextReact)
    pygame.display.update()


def gotapple():
    message_display('Your points: %d' %len(points) )

def apple(screen,RED,x,y): # drawing apple
    pygame.draw.rect(screen,(RED), (x2, y2, width, height) )

def place(x,y, xpoint, ypoint,points): #
    xpoint.insert(0,x)
    ypoint.insert(0,y)
    if len(xpoint) == (len(points)+1) and len(points) == 0:
        xpoint.pop()
        ypoint.pop()
    elif len(xpoint) > len(points):
        xpoint.pop()
        ypoint.pop()

def screenUPDATE( vel, screen ,width, height, RIGHT, LEFT, UP, DOWN):
    global x
    global y
    while RIGHT:
        x += vel
        pygame.draw.rect(screen,(255,255,255), (x, y, width, height) )
        pygame.display.update()
        screen.fill((0,0,0))
        return x
    while LEFT:
        x -= vel
        pygame.draw.rect(screen,(255,255,255), (x, y, width, height) )
        pygame.display.update()
        screen.fill((0,0,0))
        return x
    while UP:
        y -= vel
        pygame.draw.rect(screen,(255,255,255), (x, y, width, height) )
        pygame.display.update()
        screen.fill((0,0,0))
        return y
    while DOWN:
        y += vel
        pygame.draw.rect(screen,(255,255,255), (x, y, width, height) )
        pygame.display.update()
        screen.fill((0,0,0))
        return y # moving the snake

def body(x,y,vel, screen ,width, height, RIGHT, LEFT, UP, DOWN,WHITE):
    for n in range(len(points)):
        xn = xpoint[n]
        yn = ypoint[n]
        pygame.draw.rect(screen,(WHITE), (xn, yn, width, height) )

def borders():
    pygame.draw.rect(screen,(WHITE), (0, 470, 680, height) )
    pygame.draw.rect(screen,(WHITE), (0, 0, 680, height) )
    pygame.draw.rect(screen,(WHITE), (0, 0, width, 680) )
    pygame.draw.rect(screen,(WHITE), (630, 0, width, 680) )
    gotapple()


run = True
while run:
    pygame.time.delay(80)
    borders()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            DOWN = True
            UP = False
            LEFT = False
            RIGHT = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            UP = True
            DOWN = False
            LEFT = False
            RIGHT = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            UP = False
            DOWN = False
            LEFT = False
            RIGHT = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            UP = False
            DOWN = False
            RIGHT = False
            LEFT = True



    screenUPDATE( vel, screen ,width, height, RIGHT, LEFT, UP, DOWN)
    place(x,y,xpoint, ypoint,points)
    body(x,y,vel, screen ,width, height, RIGHT, LEFT, UP, DOWN,WHITE)
    apple(screen, RED,x,y)







    if x == x2 and y == y2:
        points.append(10)
        x2 = random.randrange(10,490,10)
        y2 = random.randrange(10,450,10)
        gotapple()


    if x > 620 or x < 10 or y < 10 or y > 460:
        run = False
