import pygame
import math
import time
import Options as O
import os

#initilizations
try:
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
except:
    print ('Failed To Initilize')

if pygame.get_init():
    print ('*DEBUG* - Pygame Successfully Initilized')
else:
    raise Exception('*ERROR* - Pygame Failed To Initilize')


#Pygame Variable Settings
path = 'E:\Desktop\Game Development\Turn_Based_Combat\\'
game_display = pygame.display.set_mode((O.Screen_Width,O.Screen_Height))
clock = pygame.time.Clock()
pygame.display.set_caption('Combat Tester')


#Image Loading
icon = pygame.image.load(os.path.join(path, 'Assets\Icons\Base\Hammer_Icon.png'))
background = pygame.image.load(os.path.join(path,'Assets\Backgrounds\Cartoon_Forest_BG_01\Cartoon_Forest_BG_01.png'))

#Sound Loading


#More Pygame Variables

pygame.display.set_icon(icon)

#Unit Classes
#region
class Warrior():
    """Basic Warrior Class"""
    def __init__(self, x, y, height, width, health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.health = health
        self.hitbox = pygame.rect(self.x,self.y,self.width,self.height)
    def update(self):
        pass
    def move(self):
        pass
    def take_damage(self):
        pass
    def take_heal(self):
        pass

class Mage():
    """Basic Mage Class"""
    def __init__(self, x, y, height, width, health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.health = health
        self.hitbox = pygame.rect(self.x,self.y,self.width,self.height)
    def update(self):
        pass
    def move(self):
        pass
    def take_damage(self):
        pass
    def take_heal(self):
        pass

class Archer():
    """Basic Archer Class"""
    def __init__(self, x, y, height, width, health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.health = health
        self.hitbox = pygame.rect(self.x,self.y,self.width,self.height)
    def update(self):
        pass
    def move(self):
        pass
    def take_damage(self):
        pass
    def take_heal(self):
        pass

class Ogre():
    """Basic Ogre Class"""
    def __init__(self, x, y, height, width, health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.health = health
        self.hitbox = pygame.rect(self.x,self.y,self.width,self.height)
    def update(self):
        pass
    def move(self):
        pass
    def take_damage(self):
        pass
    def take_heal(self):
        pass

class Goblin():
    """Basic Goblin Class"""
    def __init__(self, x, y, height, width, health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.health = health
        self.hitbox = pygame.rect(self.x,self.y,self.width,self.height)
    def update(self):
        pass
    def move(self):
        pass
    def take_damage(self):
        pass
    def take_heal(self):
        pass
#endregion
#Random Defenitions


#Primary Definitions

def screen_update():
    pass

#Main Menu

def main_menu():
    display = True
    #Main Menu Loop
    while display:
        #Makes it so when you hit X it closes the Program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



#Main Loop

def loop():
    loop = True
    #Game Loop
    while loop:
        #Makes it so when you hit X it closes the Program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()