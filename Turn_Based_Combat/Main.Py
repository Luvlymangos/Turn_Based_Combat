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
menu_background = [pygame.image.load(os.path.join(path, 'Assets\Backgrounds\game_background_1\layers\clouds_1.png')), 
pygame.image.load(os.path.join(path, 'Assets\Backgrounds\game_background_1\layers\clouds_2.png')), 
pygame.image.load(os.path.join(path, 'Assets\Backgrounds\game_background_1\layers\clouds_3.png')),
pygame.image.load(os.path.join(path, 'Assets\Backgrounds\game_background_1\layers\clouds_4.png')),
pygame.image.load(os.path.join(path, 'Assets\Backgrounds\game_background_1\layers\\rocks_1.png')),
pygame.image.load(os.path.join(path, 'Assets\Backgrounds\game_background_1\layers\\rocks_2.png')),
pygame.image.load(os.path.join(path, 'Assets\Backgrounds\game_background_1\layers\sky.png'))
]
buttons = pygame.image.load(os.path.join(path, 'Assets\Buttons\simple\\5.png'))
#Sound Loading

#Font Loading

Goth_Font = pygame.font.Font(os.path.join(path, 'Assets\Fonts\\04B_30__.TTF'), 60)
Title_Text = pygame.font.Font(os.path.join(path, 'Assets\Fonts\\04B_30__.TTF'), 90)
Attributions = pygame.font.SysFont('Engravers MT', 20)

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
def blit_alpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)
#Primary Definitions

def screen_update():
    pass

#Main Menu

def main_menu():
    display = True
    mos_pos = (0,0) #Init The mouse position Variable
    Paralax_Amnt = 40 #Sets the background move amount for the Parallax effect
    Fade_in_amnt = 13 #How quickly the buttons should fade in (0-254)
    Button_Alpha = 0 #Init the Alpha effect for the buttons
    Exit_Height = 900 #Exit Button Height
    Options_Height = 790 #Options Button Height
    Play_Height = 500 #Play Button Height
    global buttons
    #Main Menu Loop
    while display:
        mos_pos = pygame.mouse.get_pos() #Gets the mouse position
        #print (mos_pos) #Prints the mouse position
        #Background to Parralax
        game_display.blit(menu_background[6],(0,0))
        game_display.blit(menu_background[0],(0,0))
        game_display.blit(menu_background[1],(0,0))
        game_display.blit(menu_background[2],(0,0))
        game_display.blit(menu_background[3],(0,0))
        #Parralax Effect
        #region
        if mos_pos[0] > O.Screen_Width//2:
            blit_spot = (mos_pos[0]//Paralax_Amnt/2-240,-80)
            game_display.blit(menu_background[4],blit_spot)
        if mos_pos[0] == O.Screen_Width//2:
            blit_spot = (-160,-80)
            game_display.blit(menu_background[4],blit_spot)
        if mos_pos[0] < O.Screen_Width//2:
            blit_spot = (mos_pos[0]//Paralax_Amnt/2-240,-80)
            game_display.blit(menu_background[4],blit_spot)
        
        if mos_pos[0] > O.Screen_Width//2:
            blit_spot = (mos_pos[0]//Paralax_Amnt-240,-80)
            game_display.blit(menu_background[5],blit_spot)
        if mos_pos[0] == O.Screen_Width//2:
            blit_spot = (-160,-80)
            game_display.blit(menu_background[5],blit_spot)
        if mos_pos[0] < O.Screen_Width//2:
            blit_spot = (mos_pos[0]//Paralax_Amnt-240,-80)
            game_display.blit(menu_background[5],blit_spot)
        #endregion
        
        if Button_Alpha >= 255:
            Button_Alpha = 255
        #EXIT BUTTON
        Exit_Text = Goth_Font.render('Exit', True, [0,0,0])
        exit_button = pygame.transform.scale(buttons, (Exit_Text.get_width()+20,Exit_Text.get_height()+20))
        blit_alpha(game_display,exit_button,(O.Screen_Width/2-exit_button.get_size()[0]/2,Exit_Height),Button_Alpha)
        exit_rect = pygame.Rect(O.Screen_Width/2-exit_button.get_size()[0]/2,Exit_Height,exit_button.get_width(),exit_button.get_height())
        blit_alpha(game_display,Exit_Text,(O.Screen_Width/2-Exit_Text.get_width()/2+2,Exit_Height+7),Button_Alpha)
        #OPTIONS BUTTON
        options_Text = Goth_Font.render('Options', True, [0,0,0])
        options_button = pygame.transform.scale(buttons, (options_Text.get_width()+20,options_Text.get_height()+20))
        blit_alpha(game_display,options_button,(O.Screen_Width/2-options_button.get_size()[0]/2,Options_Height),Button_Alpha)
        options_rect = pygame.Rect(O.Screen_Width/2-options_button.get_size()[0]/2,Options_Height,options_button.get_width(),options_button.get_height())
        blit_alpha(game_display,options_Text,(O.Screen_Width/2-options_Text.get_width()/2+2,Options_Height+7),Button_Alpha)
        #PLAY BUTTON
        play_Text = Goth_Font.render('Play', True, [0,0,0])
        play_button = pygame.transform.scale(buttons, (play_Text.get_width()+20,play_Text.get_height()+20))
        blit_alpha(game_display,play_button,(O.Screen_Width/2-play_button.get_size()[0]/2,Play_Height),Button_Alpha)
        play_rect = pygame.Rect(O.Screen_Width/2-play_button.get_size()[0]/2,Play_Height,play_button.get_width(),play_button.get_height())
        blit_alpha(game_display,play_Text,(O.Screen_Width/2-play_Text.get_width()/2+2,Play_Height+7),Button_Alpha)
        #Title
        Text_Title = Title_Text.render('Swollen Legends', True, [0,0,0])
        blit_alpha(game_display,Text_Title,(O.Screen_Width/2-Text_Title.get_width()/2, O.Screen_Height/6),Button_Alpha)
        #Footer
        #game_display.blit(Attributions)
        #Handles all the events
        for event in pygame.event.get():
            #Hitting X in top right
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #On click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if  exit_rect.collidepoint(mos_pos) and Button_Alpha == 255:
                    pygame.quit()
                    quit()
                if  options_rect.collidepoint(mos_pos) and Button_Alpha == 255:
                    display = False
                    Options_Menu()
                if  play_rect.collidepoint(mos_pos) and Button_Alpha == 255:
                    display = False
                    loop()
        pygame.display.update()
        Button_Alpha += Fade_in_amnt

#Options Menu

def Options_Menu():
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
main_menu()