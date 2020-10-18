# Make sure you install pygame into your python editor, specific to your project directory. Also make sure you install from Terminal first: pip install pygame

import pygame
import random
import math
from pygame import MOUSEBUTTONDOWN

from pygame import mixer

"""Initialize pygame module so you can access its cool features and modules"""
pygame.init()

# Create the screen: 800 is width, 600 is height
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

white = (255, 255, 153)
black = (0, 0, 0)

def game_intro():
    intro = True
    click = False

    while intro:
        screen.fill(white)
        largeTextFont = pygame.font.Font('gomarice_round_pop.ttf', 90)
        intro_text = largeTextFont.render("Viralventure", True, (80, 235, 50))  # first render, then blit
        screen.blit(intro_text, (75, 100))  # middle of screen
        myfont = pygame.font.Font('gomarice_round_pop.ttf', 25)
        instructions1 = myfont.render("Help Harry collect his masks to stay alive!", True, (0, 0, 0))
        instructions2 = myfont.render("Spray hand sanitizer at curmudgeonly coronaviruses, ", True, (0, 0, 0))
        instructions22 = myfont.render("but don’t spray the masks because you need them!", True, (0, 0, 0))
        instructions3 = myfont.render("Use space bar to spray and up and down arrow keys", True, (0, 0, 0))
        instructions33 = myfont.render("to move through the store aisles.", True, (0, 0, 0))
        instructions4 = myfont.render("See how long you can help Harry stay alive", True, (0, 0, 0))
        instructions5 = myfont.render("and take down COVID-19!", True, (0, 0, 0))
        screen.blit(instructions1, (90, 200))
        screen.blit(instructions2, (40, 240))
        screen.blit(instructions22, (70, 270))
        screen.blit(instructions3, (50, 310))
        screen.blit(instructions33, (160, 340))
        screen.blit(instructions4, (110, 380))
        screen.blit(instructions5, (220, 410))
        mx, my = pygame.mouse.get_pos()
        button_start = pygame.Rect(340, 500, 100, 50)
        if button_start.collidepoint((mx, my)):
            if click:
                game_loop()

        pygame.draw.rect(screen, (80, 235, 50), button_start)

        startFont = pygame.font.Font('freesansbold.ttf', 40)
        start_text = startFont.render("Start", True, white)
        screen.blit(start_text, button_start)

        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                click = True

            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

"""screen stays for one second but then goes away, so create while loop"""

# Create bar for health
#bar_bkg = pygame.draw.rect(screen,(0, 0, 255),(200,150,100,50), 0)

# Title and Icon
""" Download icon from flaticon.com. We can design this. Select 32px version PNG."""
pygame.display.set_caption("Viralventure")  # set title
icon = pygame.image.load('virus.png')
pygame.display.set_icon(icon)  # makes sure icon has been added

# Background Image
""" 800x600 px design, with five or six aisles oriented horizontally. """
background = pygame.image.load('background.png')

# Background Sound
mixer.music.load('background.ogg')
mixer.music.play(-1) # adding -1 will make it play on loop

# Player
playerImg = pygame.image.load('bigcharacter.png')  # 64x64 PNG
playerX = 20  # x coordinate
playerY = 250  # y coordinate
playerY_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 8

# Mask
maskImg = []
maskX = []
maskY = []
maskX_change = []
maskY_change = []
num_of_masks = 4

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('virus.png'))  # 64x64 PNG
    enemyX.append(random.randint(400, 735))  # x coordinate
    enemyY.append(random.randint(70, 530))  # y coordinate
    enemyX_change.append(-40)
    enemyY_change.append(6)

# Hand Sanitizer
bulletImg = pygame.image.load('sanitizer.png')  # 32x32 PNG
bulletX = 0  # x coordinate
bulletY = 250  # y coordinate
bulletX_change = 15
bulletY_change = 0
bullet_state = "ready"
# ready - you can't see bullet on the screen
# fire - bullet is currently moving

# Mask
for i in range(num_of_masks):
    maskImg.append(pygame.image.load('face-mask.png'))  # 64x64 PNG
    maskX.append(random.randint(400, 735))  # x coordinate
    maskY.append(random.randint(70, 530))  # y coordinate
    maskX_change.append(-40)
    maskY_change.append(6)

# Score
score_value = 0
font = pygame.font.Font('gomarice_round_pop.ttf',
                        20)  # establishes free font that will be used, 32 is font size. To find other fonts, just Google free fonts of extension ttf and download them. You can go to dafont.com.

textX = 10
textY = 40


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 0, 0))  # first render, then blit
    screen.blit(score, (x, y))


# Health
health_value = 300

healthX = 300
healthY = 15

#def health_bar(screen, )
def show_health(x, y):
    pygame.draw.rect(screen,(0, 0, 0),(10,10,304,20), 0)
    pygame.draw.rect(screen,(0, 204, 0),(12,12,health_value,16), 0)

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)


def game_over_text(x, y):
    over_text = over_font.render("GAME OVER", True, (0, 0, 0))  # first render, then blit
    screen.blit(over_text, (200, 250))  # middle of screen


def player(x, y):
    screen.blit(playerImg, (x, y))  # "blit" means to draw


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def mask(x, y, i):
    screen.blit(maskImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 100, y))  # + 16 to center bullet, + 10 to make bullet fire from "top"


def isCollision(X, Y, bulletX, bulletY):
    distance = math.sqrt(math.pow(X - bulletX, 2) + math.pow(Y - bulletY, 2))  # distance formula
    if distance < 27:
        return True
    else:
        return False


def hitChar(X, Y, playerX, playerY, hitDistance):
    distance = math.sqrt(math.pow(X - playerX, 2) + math.pow(Y - playerY, 2))  # distance formula
    if distance < hitDistance:
        return True
    else:
        return False


# Game Loop
def game_loop():
    running = True
    while running:
        global bulletX
        global bulletY
        global bullet_state
        global playerY
        global playerY_change
        screen.fill((0, 0, 0))  # RGB = Red, Green, Blue
        # background image
        screen.blit(background,
                    (0, 0))  # loading background image slows down speed of player and enemy, so increase their changes
        for event in pygame.event.get():  # loop through all events happening in game window
            if event.type == pygame.QUIT:  # check to see if close button is pressed
                running = False

            """if a keystroke is pressed, check whether it's right or left"""
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    playerY_change = -8.5
                if event.key == pygame.K_DOWN:
                    playerY_change = 8.5
                if event.key == pygame.K_SPACE:
                    if bullet_state is "ready":  # ensures hitting space bar repeatedly doesn't change preexisting bullet's position
                        bullet_Sound = mixer.Sound('bulletSound.ogg')
                        bullet_Sound.play()
                        bulletY = playerY  # ensures bullet starts where Y is, but bulletY does not change when playerY does
                        fire_bullet(bulletX, bulletY)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerY_change = 0

        # Bullet Movement
        if bulletX >= 700:
            bulletX = 0
            bullet_state = "ready"
        if bullet_state is "fire":  # ensures bullet appears
            fire_bullet(bulletX, bulletY)
            bulletX += bulletX_change

        # Player Movement
        """add boundaries so player doesn't leave screen"""
        playerY += playerY_change
        if playerY <= 0:
            playerY = 0
        elif playerY >= 500:  # take into account width of rocket
            playerY = 500

        # Enemy Movement
        """add boundaries so enemy doesn't leave screen and changes direction"""
        for i in range(num_of_enemies):

            #Game Over
            global health_value
            global num_of_masks
            if health_value == 0:
                 for j in range(num_of_enemies):
                     enemyY[j] = 2000 # ensures enemies go below screen
                 for k in range(num_of_masks):
                     maskY[k] = 2000 # ensures masks go below screen
                 game_over_text(200, 250)
                 break

            enemyY[i] += enemyY_change[i]
            if enemyY[i] <= 0:
                enemyY_change[i] = 11
                enemyX[i] += enemyX_change[i]
            elif enemyY[i] >= 536:  # take into account width of enemy
                enemyY_change[i] = -11
                enemyX[i] += enemyX_change[i]

            # Collision
            global score_value
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                if bulletX == 0:
                    break
                else:
                    collisionSound = mixer.Sound('collisionSound.ogg')
                    collisionSound.play()
                    bulletX = 0  # reset bullet position
                    bullet_state = "ready"
                    score_value += 1
                    #print(score_value)
                    # respawn enemy/mask
                    enemyX[i] = random.randint(300, 735)  # x coordinate
                    enemyY[i] = random.randint(80, 500)  # y coordinate

            enemy(enemyX[i], enemyY[i], i)

            # virus hits player
            hitEnemytoChar = hitChar(enemyX[i], enemyY[i], playerX, playerY, 37)
            if hitEnemytoChar:
                virusCollide = mixer.Sound('virusCollide.ogg')
                virusCollide.play()
                health_value -= 30
                #print(health_value)
                # respawn enemy
                enemyX[i] = random.randint(300, 735)  # x coordinate
                enemyY[i] = random.randint(80, 500)  # y coordinate

            enemy(enemyX[i], enemyY[i], i)

        # Mask Movement
        for i in range(num_of_masks):
            maskY[i] += maskY_change[i]
            if maskY[i] <= 0:
                maskY_change[i] = 6
                maskX[i] += maskX_change[i]
            elif maskY[i] >= 536:  # take into account width of rocket
                maskY_change[i] = -6.0
                maskX[i] += maskX_change[i]

            # Collision
            collisionMask = isCollision(maskX[i], maskY[i], bulletX, bulletY)
            if collisionMask:
                bulletMaskCollide = mixer.Sound('bulletMaskCollide.ogg')
                bulletMaskCollide.play()
                bulletX = 0  # reset bullet position
                bullet_state = "ready"
                # respawn mask
                num_of_masks -= 1
                maskX[i] = random.randint(0, 735)  # x coordinate
                maskY[i] = random.randint(50, 150)  # y coordinate

            mask(maskX[i], maskY[i], i)

            # mask hits player
            hitMasktoChar = hitChar(maskX[i], maskY[i], playerX, playerY, 30)
            if hitMasktoChar:
                maskCollide = mixer.Sound('maskCollide.ogg')
                maskCollide.play()
                health_value += 30
                print(health_value)
                #print(playerX)
                # respawn mask
                maskX[i] = random.randint(400, 735)  # x coordinate
                maskY[i] = random.randint(80, 500)  # y coordinate

            mask(maskX[i], maskY[i], i)

        player(playerX,
               playerY)  # we want to call player after screen.fill method because we draw screen, then draw player on top
        show_score(textX, textY)
        show_health(healthX, healthY)
        pygame.display.update()  # make sure display is always updating
game_intro()
