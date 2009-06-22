# NEW-WARE-ORDER
# Destroy the New-Ware-Order
# Haroon Khalid - 06/13/2009s


import pygame
import random
import lib.setup
from sys import exit

# INITIALIZE PYGAME
pygame.init()

setup = lib.setup.Setup()
setup.run()


'''


# SET UP THE FONT AND COLOR
default_font = pygame.font.get_default_font()
font = pygame.font.SysFont(default_font, 20)
white = (255,255,255)

class Enemy(object):
    def __init__(self):
        enemy = 'enemy.png'
        enemyimg = pygame.image.load(enemy).convert()
        enemyimg.set_colorkey((76,88,100))
        self.image = enemyimg
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
    
    def update(self):
        if self.rect.x < 100:
            enemies.remove(self)
        else:
            self.rect.x -= 1
            screen.blit(self.image, (self.rect.x,self.rect.y))

class Bullet(object):
    def __init__(self):
        bullet = 'bullet.png'
        bulletimg = pygame.image.load(bullet).convert()
        self.image = bulletimg
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        
    def update(self):
        if self.rect.x > 300:
            bullets.remove(self)
        else:
            self.rect.x += 10
            screen.blit(bulletimg,(self.rect.x,self.rect.y))

class Player(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.alive = True
        player = 'player.png'
        playerimg = pygame.image.load(player).convert()
        self.image = playerimg

def test_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shot_snd.play()
                create_bullet()
            if event.key == pygame.K_z:
                create_enemy()

def draw_stats():
    white = (255, 255, 255)
    bulletamt = str(len(bullets))
    bullettxt = font.render("Bullets: " + bulletamt, True, white)
    enemyamt = str(len(enemies))
    enemytxt = font.render("Enemies: " + enemyamt, True, white)
    screen.blit(enemytxt, (1, 1))    
    screen.blit(bullettxt, (1, 14))
    
def create_enemy():
    E = Enemy()
    E.rect.x = random.randint(200,250)  
    E.rect.y = 0
    enemies.append(E)
    
def update_enemy():
    for enemy in enemies:
        enemy.update()

def create_bullet():
    b = Bullet()
    b.rect.x = p1.x + 25
    b.rect.y = p1.y + 7
    bullets.append(b)

def update_bullet():
    for bullet in bullets:
        bullet.update()

# CHECK FOR COLLISION BY COMPARING RECTS W/ LISTS
def check_hit():
    for j in bullets:
        for k in enemies:
            if j.rect.colliderect(k.rect):
                zap_snd.play()
                if j in bullets:
                    bullets.remove(j)
                if k in enemies:
                    enemies.remove(k)

# SOUNDS
shot_snd = pygame.mixer.Sound("shot.ogg")
hit_snd = pygame.mixer.Sound("hit.ogg")
zap_snd = pygame.mixer.Sound("zap.ogg")

# LISTS FOR STORING 
bullets = []
enemies = []

# CREATE THE PLAYERS SHIP AND POSITION
p1 = Player()
p1.x = 0
p1.y = 29

# SETTING UP SPRITES
bullet = 'bullet.png'
bulletimg = pygame.image.load(bullet).convert()
bg = 'bg.png'
bgimg = pygame.image.load(bg).convert()

# MAIN GAME LOOP
while True:
    
    screen.blit(bgimg, (0,0))
    draw_stats()
    test_input()
    check_hit()
    screen.blit(p1.image, (p1.x, p1.y))
    update_bullet()
    update_enemy()
    pygame.display.update()
    pygame.time.delay(25)

'''
