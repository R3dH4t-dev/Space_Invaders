import random
import math
import pygame

#Agradecimentos pelos sprites: Freepik, Smashicons, Pixel Buddha and Flaticon.com

# Init the pygame
pygame.init()

#Criar a Janela 800w x 600h
screen = pygame.display.set_mode((800,600))

#Background
background = pygame.image.load('background.jpg')

#Titulo e Ícone
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('download.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 480
playerX_change = 0

#Enemies
enemy_1 = []
enemy1_X = []
enemy1_Y = []
enemy1_changeX = []
enemy1_changeY = []
num = 6

#Score
score = 0
font = pygame.font.Font("8bit.ttf", 18)
textX = 10
textY = 10

def show_score(x, y):
    score_value = font.render("Score " + str(score), True, (255, 255, 255))
    screen.blit(score_value, (x,y))


for i in range(num):
    if (i % 2 == 0):
        enemy_1.append(pygame.image.load("alien1.png"))
        enemy1_X.append(random.randint(0, 750))
        enemy1_Y.append(random.randint(50, 150))
        enemy1_changeX.append(3)
        enemy1_changeY.append(35)
    elif (i % 3 == 0):
        enemy_1.append(pygame.image.load("alien2.png"))
        enemy1_X.append(random.randint(0, 750))
        enemy1_Y.append(random.randint(50, 150))
        enemy1_changeX.append(3)
        enemy1_changeY.append(35)
    else:
        enemy_1.append(pygame.image.load("alien3.png"))
        enemy1_X.append(random.randint(0, 750))
        enemy1_Y.append(random.randint(50, 150))
        enemy1_changeX.append(3)
        enemy1_changeY.append(35)

#Bullet - State: True the bullet is ready / False you're already shooting
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 15
bullet_state = False


#Função que chama a playerImg nas coordenadas X e Y
def player(x,y):
    screen.blit(playerImg, (x, y))

def enemies (x,y,n):
    for u in range(n):
        screen.blit(enemy_1[u], (x, y))

def bullet_fire (x, y):
    global bullet_state
    bullet_state = True
    screen.blit(bulletImg, (x-3, y+10))
    screen.blit(bulletImg, (x+48, y+10))

def isCollision(x1, y1, x2, y2):
    distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
    if distance < 40:
        return True
    else:
        return False


#Game Loop
running = True
while running:

    # RGB - Background
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #If Tecla = pressed Cheque se foi Right, Left ou Space
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -5
        if event.key == pygame.K_RIGHT:
            playerX_change = 5
        if event.key == pygame.K_SPACE:
           if bullet_state == False:
             #Pega as coordenadas da Nave no momento do tiro
                bulletX = playerX
                bullet_fire(bulletX, bulletY)


    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0



    playerX += playerX_change

    if playerX <= -4:
        playerX = -4
    elif playerX >= 741:
        playerX = 741


    for i in range(num):

        enemy1_X[i] += enemy1_changeX[i]
        if enemy1_X[i] <= -4:
            enemy1_changeX[i] = 3
            enemy1_Y[i] += enemy1_changeY[i]
        elif enemy1_X[i] >= 741:
            enemy1_changeX[i] = -3
            enemy1_Y[i] += enemy1_changeY[i]

        #Teste de colisão
        collision = isCollision(enemy1_X[i], enemy1_Y[i], bulletX, bulletY)
        if collision == True:
            bullet_state = False
            bulletY = 480
            score += 100
            enemy1_X[i] = random.randint(0, 750)
            enemy1_Y[i] = random.randint(50, 150)



        enemies(enemy1_X[i], enemy1_Y[i], i)


    #Bullet Movement
    if bullet_state == True:
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_change
    if bulletY<-5:
        bulletY = 480
        bullet_state = False




    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
