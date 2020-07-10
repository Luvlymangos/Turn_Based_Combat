import pygame
import math
import time
import Options as O
import os
import Warrior as W
import Sprite_Dict as S
import Event_List as E
#initilizations
try:
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    pygame.mixer.pre_init(44100, -16, 2, 512)
except:
    print ('Failed To Initilize')

if pygame.get_init():
    print ('*DEBUG* - Pygame Successfully Initilized')
else:
    raise Exception('*ERROR* - Pygame Failed To Initilize')



#Pygame Variable Settings
vec = pygame.math.Vector2
path = 'E:\Desktop\Game Development\Turn_Based_Combat\\'
game_display = pygame.display.set_mode((O.Screen_Width,O.Screen_Height))
clock = pygame.time.Clock()
pygame.display.set_caption('Combat Tester')
all_sprites = pygame.sprite.Group()
Collidables = pygame.sprite.Group()
Decor = pygame.sprite.Group()
Event = pygame.sprite.Group()
Base = []
clouds = []
inventory = []
Clouds_num = 0


#Image Loading
doa = pygame.image.load(os.path.join(path, 'Assets\Icons\Base\DOA.png'))
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
Sound_icon = [pygame.image.load(os.path.join(path, 'Assets\Icons\Base\Sound_play.png')), 
pygame.image.load(os.path.join(path, 'Assets\Icons\Base\Sound_Mute.png'))]
base_image = pygame.image.load(os.path.join(path, 'Assets\Tilemap\\bg.png'))
Bubble = pygame.image.load(os.path.join(path, 'Assets\Warrior\Text_Bubble\popup_1.png'))
Sword_Image = pygame.image.load(os.path.join(path, 'Assets\Icons\Base\Gold_Coins.png'))
Warrior1_idle_Frames = []
for i in W.Warrior_1_idle:
    Warrior1_idle_Frames.append(pygame.transform.scale(i,(250,340)))
Warrior1_Game_Idle_Frames = []
for i in W.Warrior_1_idle:
    Warrior1_Game_Idle_Frames.append(pygame.transform.scale(i,(128,177)))

Warrior2_idle_Frames = []
for i in W.Warrior_2_idle:
    Warrior2_idle_Frames.append(pygame.transform.scale(i,(250,340)))
Warrior2_Game_Idle_Frames = []
for i in W.Warrior_2_idle:
    Warrior2_Game_Idle_Frames.append(pygame.transform.scale(i,(128,177)))

Warrior3_idle_Frames = []
for i in W.Warrior_3_idle:
    Warrior3_idle_Frames.append(pygame.transform.scale(i,(250,340)))
Warrior3_Game_Idle_Frames = []
for i in W.Warrior_3_idle:
    Warrior3_Game_Idle_Frames.append(pygame.transform.scale(i,(128,177)))
Warrior1_Right_Walk = W.Warrior_1_right
Warrior1_Left_Walk = W.Warrior_1_left
Warrior1_Down_Walk = W.Warrior_1_down
Warrior1_Up_Walk = W.Warrior_1_up
Warrior2_Right_Walk = W.Warrior_2_right 
Warrior2_Left_Walk = W.Warrior_2_left
Warrior2_Down_Walk = W.Warrior_2_down
Warrior2_Up_Walk = W.Warrior_2_up
Warrior3_Right_Walk = W.Warrior_3_right 
Warrior3_Left_Walk = W.Warrior_3_left
Warrior3_Down_Walk = W.Warrior_3_down
Warrior3_Up_Walk = W.Warrior_3_up


#Sound Loading

on_hover_sound = pygame.mixer.Sound(os.path.join(path, 'Assets\Sounds\hover_over.wav'))
pygame.mixer.music.load(os.path.join(path, 'Assets\Music\Amadeus - Legendary.wav'))

#Font Loading
Options_Lesser_Font = pygame.font.Font(os.path.join(path, 'Assets\Fonts\\04B_30__.TTF'), 25)
Options_Font = pygame.font.Font(os.path.join(path, 'Assets\Fonts\\04B_30__.TTF'), 40)
Goth_Font = pygame.font.Font(os.path.join(path, 'Assets\Fonts\\04B_30__.TTF'), 60)
Title_Text = pygame.font.Font(os.path.join(path, 'Assets\Fonts\\04B_30__.TTF'), 90)
Attributions = pygame.font.SysFont('Engravers MT', 25)

#More Pygame Variables

pygame.display.set_icon(icon)

#Map Classes
class Base_Sprite():
    def __init__(self, x, y):
        Base.append(self)
        self.image = base_image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * O.Tile_Size
        self.rect.y = y * O.Tile_Size

class New_Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, num, Collidable=False):
        if Collidable == True:
            self.groups = all_sprites, Collidables
        else:
            self.groups = all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = W.Sprite_All[int(num)]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * O.Tile_Size
        self.rect.y = y * O.Tile_Size

class New_Decor(pygame.sprite.Sprite):
    def __init__(self, x, y, num, Collidable=False, Event_add=False):
        if Event_add == True:
            self.groups = Decor, Event
        elif Collidable == True:
            self.groups = Decor, Collidables
        else:
            self.groups = Decor
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = W.Building[int(num)]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.pos = vec(x, y) * O.Tile_Size
        self.rect.x = x * O.Tile_Size
        self.rect.y = y * O.Tile_Size
    def event_run(self):
        inventory.append(Sword(5,Sword_Image))
        inventory.append(Sword(5,Sword_Image))
#Item Definitions
class Sword():
    def __init__(self, Damage, Image):
        self.Damage = Damage
        self.Image = Image
        self.Icon = pygame.transform.scale(self.Image,(64,64))

#Random Defenitions
def blit_alpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)

def load_data(self):
        game_folder = path.dirname(__file__)
        map = Map(path.join(game_folder, 'map2.txt'))


#Primary Definitions
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image, name):
        self.groups = all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        if image == '1':
            self.armor = 1
            self.image = Warrior1_Game_Idle_Frames[0]
        if image == '2':
            self.armor = 2
            self.image = Warrior2_Game_Idle_Frames[0]
        if image == '3':
            self.armor = 3
            self.image = Warrior3_Game_Idle_Frames[0]
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * O.Tile_Size
        self.speed = 0.20
        self.rect = self.image.get_rect()

    
    def update(self):
        self.pos += self.vel * clock.tick(O.Screen_Updates)
        self.rect.x = self.pos.x
        self.collide_with_walls('x')
        self.rect.y = self.pos.y
        self.collide_with_walls('y')
        self.vel = vec(0,0)
        self.collide_with_event('x')
        self.collide_with_event('y')
        
    def animate(self,frame):
        if self.vel.x == 0 and self.vel.y == 0:
            if self.armor == 1:
                self.image = Warrior1_Game_Idle_Frames[frame//1]
            if self.armor == 2:
                self.image = Warrior2_Game_Idle_Frames[frame//1]
            if self.armor == 3:
                self.image = Warrior3_Game_Idle_Frames[frame//1]
        if self.vel.x > 0:
            if self.armor == 1:    
                self.image = Warrior1_Right_Walk[frame//1]
            if self.armor == 2:
                self.image = Warrior2_Right_Walk[frame//1]
            if self.armor == 3:
                self.image = Warrior3_Right_Walk[frame//1]
        if self.vel.x < 0:
            if self.armor == 1:
                self.image = Warrior1_Left_Walk[frame//1]
            if self.armor == 2:
                self.image = Warrior2_Left_Walk[frame//1]
            if self.armor == 3:
                self.image = Warrior3_Left_Walk[frame//1]
        if self.vel.y > 0:
            if self.armor == 1:
                self.image = Warrior1_Down_Walk[frame//1]
            if self.armor == 2:
                self.image = Warrior2_Down_Walk[frame//1]
            if self.armor == 3:
                self.image = Warrior3_Down_Walk[frame//1]
        if self.vel.y < 0:
            if self.armor == 1:
                self.image = Warrior1_Up_Walk[frame//1]
            if self.armor == 2:
                self.image = Warrior2_Up_Walk[frame//1]
            if self.armor == 3:
                self.image = Warrior3_Up_Walk[frame//1]
    
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pygame.sprite.spritecollide(self, Collidables, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
        if dir == 'y':
            hits = pygame.sprite.spritecollide(self, Collidables, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y
    def collide_with_event(self,dir):
        if dir == 'x':
            hits = pygame.sprite.spritecollide(self, Event, True)
            if hits:
                for i in hits:
                    i.event_run()
        if dir == 'y':
            hits = pygame.sprite.spritecollide(self, Event, True)
            if hits:
                for i in hits:
                    i.event_run()



class Map:
    def __init__(self, filename, Dfilename):
        self.data = []
        self.ddata = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())
        with open(Dfilename, 'rt') as d:
            for line in d:
                self.ddata.append(line.strip())
        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * O.Tile_Size
        self.height = self.tileheight * O.Tile_Size

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(O.Screen_Width / 2)
        y = -target.rect.y + int(O.Screen_Height / 2)
        self.x = x
        self.y = y
        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - O.Screen_Width), x)  # right
        y = max(-(self.height - O.Screen_Height), y)  # bottom
        self.camera = pygame.Rect(x, y, self.width, self.height)       
class Clouds:
    def __init__(self, x, y, image, current):
        self.current = current
        self.x = x
        self.y = y
        self.image = image
    def update(self):
        self.x += self.current
        game_display.blit(self.image, (self.x, self.y))
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = [0,0,0]
        self.txt_surface = Options_Font.render(text, True, self.color)
        self.active = False
        self.saved_text = ''

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.saved_text = self.text
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                    self.saved_text = self.text
                # Re-render the text.
                if len(self.text) > 15:
                    self.text = self.text[:-1]
                self.txt_surface = Options_Font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        exit_button = pygame.transform.scale(buttons, (self.rect.w+20,self.rect.h+20))
        screen.blit(exit_button,(self.rect.x-5,self.rect.y-5))
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        if self.active:
            Box_Rect = pygame.Rect(self.rect.x-5,self.rect.y-5,self.rect.w+20,self.rect.h+20)
            pygame.draw.rect(game_display,[0,0,0],Box_Rect,2)
    def has_text(self):
        if self.text != '':
            return False
        else:
            return True
    def get_text(self):
        return self.saved_text
        
def inventory_open():
    display = True
    Back_Height = 900
    print('Opening Inventory')
    Inv_Text = Options_Lesser_Font.render('Inventory', True, (255,255,255))
    Bag_Rect = pygame.Surface((450,500))
    Bag_Rect.set_alpha(64)
    Bag_Out_rect = pygame.Rect(1130,450,450,500)
    Bag_Rect.fill((0,0,0))
    game_display.blit(Bag_Rect,(1130,450))
    pygame.draw.rect(game_display,(0,0,0),Bag_Out_rect, 1)
    game_display.blit(Inv_Text,(1135,460))
    while display:
        #Back Button
        mos_pos = pygame.mouse.get_pos()
        Back_Text = Goth_Font.render('Back', True, [0,0,0])
        back_button = pygame.transform.scale(buttons, (Back_Text.get_width()+20,Back_Text.get_height()+20))
        game_display.blit(back_button,(O.Screen_Width/2-back_button.get_size()[0]/2,Back_Height))
        back_rect = pygame.Rect(O.Screen_Width/2-back_button.get_size()[0]/2,Back_Height,back_button.get_width(),back_button.get_height())
        game_display.blit(Back_Text,(O.Screen_Width/2-Back_Text.get_width()/2+2,Back_Height+7))
        x = 1150 
        y = 500
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(mos_pos):
                    display = False
        for l in inventory:
            print (len(inventory))
            box = pygame.Rect(x,y, 64, 64)
            if x == 1450:
                x = 1200
                y += 80
            if y >= 980:
                pass
            else:
                pygame.draw.rect(game_display, [0,0,0], box, 1)
                game_display.blit(l.Icon,(x+box[2]-l.Icon.get_width(),y+box[3]-l.Icon.get_height()))

                x += 80
        pygame.display.update()

def screen_update(camera, player):
    Backfill = pygame.Rect(0,0, O.Screen_Width, O.Screen_Height)
    pygame.draw.rect(game_display,[0,0,0], Backfill)
    for sprite in Base:
        game_display.blit(sprite.image, camera.apply(sprite))
    for sprite in all_sprites:
        if sprite != player:
            game_display.blit(sprite.image, camera.apply(sprite))
    for sprite in all_sprites:
        if sprite == player:
            game_display.blit(sprite.image, camera.apply(sprite))
    for sprite in Decor:
        game_display.blit(sprite.image, camera.apply(sprite))
    for sprite in Event:
        pygame.draw.rect(game_display, [0,0,0], sprite.rect, 3)
    player.update()
    camera.update(player)
    pygame.display.update() #Make sure this is at the bottom of screen_update()
    clock.tick(O.Screen_Updates)
#Startup Splash

def Startup_Splash():
    display = True
    alpha = 0
    frame = 0
    neg_alpha = 255
    while display:
        #Controls the fade in of the logo and text
        if alpha >= 255:
            alpha = 255
            #Fades out the logo and text
            if alpha == 255 and frame > 200:
                neg_alpha -= 2
                game_display.fill([0,0,0])
                DOA = Goth_Font.render('Dissolution Of Assets', True, [255,255,255])
                blit_alpha(game_display,DOA,(O.Screen_Width/2-DOA.get_width()/2,700),neg_alpha)
                blit_alpha(game_display,doa,(O.Screen_Width/2-doa.get_width()/2,350),neg_alpha)
                pygame.display.update()

        else:
            game_display.fill([0,0,0])
            DOA = Goth_Font.render('Dissolution Of Assets', True, [255,255,255])
            blit_alpha(game_display,DOA,(O.Screen_Width/2-DOA.get_width()/2,700),alpha)
            blit_alpha(game_display,doa,(O.Screen_Width/2-doa.get_width()/2,350),alpha)
            pygame.display.update()
            alpha += 2
        frame += 1
        for event in pygame.event.get():
            #Hitting X in top right
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #Starts up the main menu
        if frame > 400 or neg_alpha <= 0:
            display = False
            main_menu()
        clock.tick(O.Screen_Updates)
#Main Menu

def main_menu(First=True):
    global Clouds_num
    display = True
    mos_pos = (0,0) #Init The mouse position Variable
    Paralax_Amnt = 40 #Sets the background move amount for the Parallax effect
    Fade_in_amnt = 15 #How quickly the buttons should fade in (0-254)
    if First == True:
        Button_Alpha = 0 #Init the Alpha effect for the buttons
        pygame.mixer.music.play()
    else:
        Button_Alpha = 255
    Exit_Height = 900 #Exit Button Height
    Options_Height = 790 #Options Button Height
    Play_Height = 500 #Play Button Height
    sound_cooldown = 5
    Cloud_Off = 1.5
    Muted = O.Muted
    global buttons
    #Main Menu Loop
    while display:
        game_display.blit(menu_background[6],(0,0))
        game_display.blit(menu_background[0],(-320,0))
        if Clouds_num % 1920 == 0:
            clouds.append(Clouds(-1920, 0, menu_background[2], Cloud_Off/2))
            clouds.append(Clouds(-1920, 0, menu_background[3], Cloud_Off/3))
            clouds.append(Clouds(-1920, 0, menu_background[1], Cloud_Off))
        
        if len(clouds) > 6:
            clouds.pop()
        for i in clouds:
            i.update()
            if i.x > 1920:
                clouds.remove(i)
        pygame.mixer.music.set_volume(O.Volume)
        mos_pos = pygame.mouse.get_pos() #Gets the mouse position
        #Background to Parralax
        #Parralax Effect
        #region
        if mos_pos[0] > O.Screen_Width//2:
            blit_spot = (mos_pos[0]//Paralax_Amnt/2-240,-56)
            game_display.blit(menu_background[4],blit_spot)
        if mos_pos[0] == O.Screen_Width//2:
            blit_spot = (-160,-80)
            game_display.blit(menu_background[4],blit_spot)
        if mos_pos[0] < O.Screen_Width//2:
            blit_spot = (mos_pos[0]//Paralax_Amnt/2-240,-56)
            game_display.blit(menu_background[4],blit_spot)
        
        if mos_pos[0] > O.Screen_Width//2:
            blit_spot = (mos_pos[0]//Paralax_Amnt-240,-56)
            game_display.blit(menu_background[5],blit_spot)
        if mos_pos[0] == O.Screen_Width//2:
            blit_spot = (-160,-80)
            game_display.blit(menu_background[5],blit_spot)
        if mos_pos[0] < O.Screen_Width//2:
            blit_spot = (mos_pos[0]//Paralax_Amnt-240,-56)
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
        Footer_Text = Attributions.render('Made by Luvlymangos & John Geary Blackjack', True, [255,255,255])
        game_display.blit(Footer_Text, (O.Screen_Width-Footer_Text.get_width(),O.Screen_Height-Footer_Text.get_height()))
        mute_rect = pygame.Rect(0,O.Screen_Height-Sound_icon[0].get_height(),Sound_icon[0].get_width(),Sound_icon[0].get_height())
        if not Muted:
            game_display.blit(Sound_icon[0],(0,O.Screen_Height-Sound_icon[0].get_height()))
            pygame.mixer.music.unpause()
        if Muted:
            game_display.blit(Sound_icon[1],(0,O.Screen_Height-Sound_icon[0].get_height()))
            pygame.mixer.music.pause()
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
                    Char_Screen()
                if mute_rect.collidepoint(mos_pos) and Muted == False:
                    Muted = True
                    O.Muted = True
                elif mute_rect.collidepoint(mos_pos) and Muted == True:
                    Muted = False
                    O.Muted = False
        if  exit_rect.collidepoint(mos_pos) and Button_Alpha == 255 and sound_cooldown <= 0:
            on_hover_sound.play()
            sound_cooldown = 20
        if  options_rect.collidepoint(mos_pos) and Button_Alpha == 255 and sound_cooldown <= 0:
            on_hover_sound.play()
            sound_cooldown = 20
        if  play_rect.collidepoint(mos_pos) and Button_Alpha == 255 and sound_cooldown <= 0:
            on_hover_sound.play()
            sound_cooldown = 20
        if  exit_rect.collidepoint(mos_pos) and Button_Alpha == 255:
            pygame.draw.rect(game_display,[255,255,255,1],exit_rect,3)
        if  options_rect.collidepoint(mos_pos) and Button_Alpha == 255:
            pygame.draw.rect(game_display,[255,255,255,1],options_rect,3)
        if  play_rect.collidepoint(mos_pos) and Button_Alpha == 255:
            pygame.draw.rect(game_display,[255,255,255,1],play_rect,3)
        pygame.display.update()
        clock.tick(O.Screen_Updates)
        Button_Alpha += Fade_in_amnt
        sound_cooldown -= 1
        Clouds_num += Cloud_Off

#Options Menu

def Options_Menu():
    display = True
    mos_pos = (0,0) #Init The mouse position Variable
    Paralax_Amnt = 40 #Sets the background move amount for the Parallax effect
    Muted = O.Muted
    sound_cooldown = 5
    Volume_Grab = False
    global Clouds_num
    Cloud_Off = 1.5
    Back_Height = 900 #Back Button Height
    while display:
        pygame.mixer.music.set_volume(O.Volume)
        mos_pos = pygame.mouse.get_pos() #Gets the mouse position
        #Background to Parralax
        game_display.blit(menu_background[6],(0,0))
        game_display.blit(menu_background[0],(-320,0))
        if Clouds_num % 1920 == 0:
            clouds.append(Clouds(-1920, 0, menu_background[2], Cloud_Off/2))
            clouds.append(Clouds(-1920, 0, menu_background[3], Cloud_Off/3))
            clouds.append(Clouds(-1920, 0, menu_background[1], Cloud_Off))
        if len(clouds) > 6:
            clouds.pop()
        for i in clouds:
            i.update()
            if i.x > 1920:
                clouds.remove(i)
        #Parralax Effect
        #region
        if mos_pos[0] > O.Screen_Width//2:
            blit_spot = (mos_pos[0]//Paralax_Amnt/2-240,-56)
            game_display.blit(menu_background[4],blit_spot)
        if mos_pos[0] == O.Screen_Width//2:
            blit_spot = (-160,-80)
            game_display.blit(menu_background[4],blit_spot)
        if mos_pos[0] < O.Screen_Width//2:
            blit_spot = (mos_pos[0]//Paralax_Amnt/2-240,-56)
            game_display.blit(menu_background[4],blit_spot)
        
        if mos_pos[0] > O.Screen_Width//2:
            blit_spot = (mos_pos[0]//Paralax_Amnt-240,-56)
            game_display.blit(menu_background[5],blit_spot)
        if mos_pos[0] == O.Screen_Width//2:
            blit_spot = (-160,-80)
            game_display.blit(menu_background[5],blit_spot)
        if mos_pos[0] < O.Screen_Width//2:
            blit_spot = (mos_pos[0]//Paralax_Amnt-240,-56)
            game_display.blit(menu_background[5],blit_spot)
        #endregion
        #TITLE TEXT
        Text_Title = Goth_Font.render('Options', True, [0,0,0])
        game_display.blit(Text_Title,(O.Screen_Width/2-Text_Title.get_width()/2, O.Screen_Height/15))
        #Volume Slider
        Text_Volume = Options_Font.render('Volume',True, [0,0,0])
        Text_Raw_Volume = Options_Lesser_Font.render("{:.2f}%".format(O.Volume*100),True, [0,0,0])
        Slider_base = pygame.Rect(O.Screen_Width/2-250,O.Screen_Height/4,500,5)
        pygame.draw.rect(game_display,[0,0,0],Slider_base)
        game_display.blit(Text_Volume,(O.Screen_Width/2-Text_Volume.get_width()/2,O.Screen_Height/4-Text_Volume.get_height()-10))
        game_display.blit(Text_Raw_Volume,(O.Screen_Width/2-Text_Raw_Volume.get_width()/2,O.Screen_Height/4-Text_Raw_Volume.get_height()+40))
        Slider_Mover = pygame.Rect(O.Screen_Width/2-250+(500*O.Volume),O.Screen_Height/4-7,20,20)
        pygame.draw.rect(game_display,[255,255,255],Slider_Mover)
        #BACK BUTTON
        Back_Text = Goth_Font.render('Back', True, [0,0,0])
        back_button = pygame.transform.scale(buttons, (Back_Text.get_width()+20,Back_Text.get_height()+20))
        game_display.blit(back_button,(O.Screen_Width/2-back_button.get_size()[0]/2,Back_Height))
        back_rect = pygame.Rect(O.Screen_Width/2-back_button.get_size()[0]/2,Back_Height,back_button.get_width(),back_button.get_height())
        game_display.blit(Back_Text,(O.Screen_Width/2-Back_Text.get_width()/2+2,Back_Height+7))
        #Footer
        Footer_Text = Attributions.render('Made by Luvlymangos & John Geary Blackjack', True, [255,255,255])
        game_display.blit(Footer_Text, (O.Screen_Width-Footer_Text.get_width(),O.Screen_Height-Footer_Text.get_height()))
        mute_rect = pygame.Rect(0,O.Screen_Height-Sound_icon[0].get_height(),Sound_icon[0].get_width(),Sound_icon[0].get_height())
        if not Muted:
            game_display.blit(Sound_icon[0],(0,O.Screen_Height-Sound_icon[0].get_height()))
            pygame.mixer.music.unpause()
        if Muted:
            game_display.blit(Sound_icon[1],(0,O.Screen_Height-Sound_icon[0].get_height()))
            pygame.mixer.music.pause()
        for event in pygame.event.get():
            #Hitting X in top right
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mute_rect.collidepoint(mos_pos) and Muted == False:
                    Muted = True
                    O.Muted = True
                elif mute_rect.collidepoint(mos_pos) and Muted == True:
                    Muted = False
                    O.Muted = False
                if  back_rect.collidepoint(mos_pos):
                    display = False
                    main_menu(First=False)
                if Slider_Mover.collidepoint(mos_pos):
                    Volume_Grab = True   
            if event.type == pygame.MOUSEBUTTONUP:
                Volume_Grab = False
            if event.type == pygame.MOUSEMOTION and Volume_Grab:
                amnt_to_Move = pygame.mouse.get_rel()
                O.Volume = O.Volume
                O.Volume += amnt_to_Move[0]/500
                amnt_to_Move = 0
        if O.Volume > 1:
            O.Volume = 1
        if O.Volume < 0:
            O.Volume = 0
        if  back_rect.collidepoint(mos_pos) and sound_cooldown <= 0:
            on_hover_sound.play()
            sound_cooldown = 20
        if  back_rect.collidepoint(mos_pos):
            pygame.draw.rect(game_display,[255,255,255,1],back_rect,3)
        sound_cooldown -= 1
        pygame.display.update()
        clock.tick(O.Screen_Updates)
        Clouds_num += 1.5

#Character Selection Screen
def Char_Screen():
    display = True
    mos_pos = (0,0) #Init The mouse position Variable
    Paralax_Amnt = 40 #Sets the background move amount for the Parallax effect
    Muted = O.Muted
    Frame = 0
    global Clouds_num
    Cloud_Off = 1.5
    sound_cooldown = 5
    Back_Height = 900 #Back Button Height
    play_Height = 800
    Char_Name = InputBox(O.Screen_Width/2, O.Screen_Height/2-400, 300, 50)
    Warrior_Type = 1
    while display:
        if Frame > 58:
            Frame = 0
        pygame.mixer.music.set_volume(O.Volume)
        mos_pos = pygame.mouse.get_pos() #Gets the mouse position
        #Background to Parralax
        game_display.blit(menu_background[6],(0,0))
        game_display.blit(menu_background[0],(-320,0))
        if Clouds_num % 1920 == 0:
            clouds.append(Clouds(-1920, 0, menu_background[2], Cloud_Off/2))
            clouds.append(Clouds(-1920, 0, menu_background[3], Cloud_Off/3))
            clouds.append(Clouds(-1920, 0, menu_background[1], Cloud_Off))
        if len(clouds) > 6:
            clouds.pop()
        for i in clouds:
            i.update()
            if i.x > 1920:
                clouds.remove(i)
        #Parralax Effect
        #region
        if mos_pos[0] > O.Screen_Width//2:
            blit_spot = (mos_pos[0]//Paralax_Amnt/2-240,-56)
            game_display.blit(menu_background[4],blit_spot)
        if mos_pos[0] == O.Screen_Width//2:
            blit_spot = (-160,-80)
            game_display.blit(menu_background[4],blit_spot)
        if mos_pos[0] < O.Screen_Width//2:
            blit_spot = (mos_pos[0]//Paralax_Amnt/2-240,-56)
            game_display.blit(menu_background[4],blit_spot)
        
        if mos_pos[0] > O.Screen_Width//2:
            blit_spot = (mos_pos[0]//Paralax_Amnt-240,-56)
            game_display.blit(menu_background[5],blit_spot)
        if mos_pos[0] == O.Screen_Width//2:
            blit_spot = (-160,-80)
            game_display.blit(menu_background[5],blit_spot)
        if mos_pos[0] < O.Screen_Width//2:
            blit_spot = (mos_pos[0]//Paralax_Amnt-240,-56)
            game_display.blit(menu_background[5],blit_spot)
        #endregion
        #BACK BUTTON
        Back_Text = Goth_Font.render('Back', True, [0,0,0])
        back_button = pygame.transform.scale(buttons, (Back_Text.get_width()+20,Back_Text.get_height()+20))
        game_display.blit(back_button,(O.Screen_Width/2-back_button.get_size()[0]/2,Back_Height))
        back_rect = pygame.Rect(O.Screen_Width/2-back_button.get_size()[0]/2,Back_Height,back_button.get_width(),back_button.get_height())
        game_display.blit(Back_Text,(O.Screen_Width/2-Back_Text.get_width()/2+2,Back_Height+7))
        #Footer
        Footer_Text = Attributions.render('Made by Luvlymangos & John Geary Blackjack', True, [255,255,255])
        game_display.blit(Footer_Text, (O.Screen_Width-Footer_Text.get_width(),O.Screen_Height-Footer_Text.get_height()))
        mute_rect = pygame.Rect(0,O.Screen_Height-Sound_icon[0].get_height(),Sound_icon[0].get_width(),Sound_icon[0].get_height())
        #CHARACTER NAME
        Char_Name.update()
        Char_Name.draw(game_display)
        Character_Name = Options_Font.render('Character Name:', True, [0,0,0])
        game_display.blit(Character_Name,(O.Screen_Width/2-Character_Name.get_width()-10, O.Screen_Height/2-400+Character_Name.get_height()/4))
        #CHARACTER DISPLAY
        Left = Goth_Font.render('<', True, [0,0,0])
        Right = Goth_Font.render('>', True, [0,0,0])
        Left_button = pygame.transform.scale(buttons, (Left.get_width()+20,Left.get_height()+20))
        Right_button = pygame.transform.scale(buttons, (Right.get_width()+20,Right.get_height()+20))
        Left_rect = pygame.Rect(O.Screen_Width/2-200,O.Screen_Height/2-Left_button.get_height()/2,Left.get_width()+20,Left.get_height()+20)
        Right_rect = pygame.Rect(O.Screen_Width/2+200-55,O.Screen_Height/2-Right_button.get_height()/2,Right.get_width()+20,Right.get_height()+20)
        game_display.blit(Left_button,(O.Screen_Width/2-200,O.Screen_Height/2-Left_button.get_height()/2))
        game_display.blit(Left,(O.Screen_Width/2-200+Left.get_width()/2,O.Screen_Height/2-Left.get_height()/2-5))
        game_display.blit(Right_button,(O.Screen_Width/2+200-55,O.Screen_Height/2-Right_button.get_height()/2))
        game_display.blit(Right,(O.Screen_Width/2+200+Right.get_width()/2-55,O.Screen_Height/2-Right.get_height()/2-5))
        if Warrior_Type == 1:
            game_display.blit(Warrior1_idle_Frames[Frame//2],(O.Screen_Width/2-Warrior1_idle_Frames[0].get_width()/2,300))
        if Warrior_Type == 2:
            game_display.blit(Warrior2_idle_Frames[Frame//2],(O.Screen_Width/2-Warrior2_idle_Frames[0].get_width()/2,300))
        if Warrior_Type == 3:
            game_display.blit(Warrior3_idle_Frames[Frame//2],(O.Screen_Width/2-Warrior3_idle_Frames[0].get_width()/2,300))
        if not Char_Name.has_text():
            Play_Text = Goth_Font.render('Play', True, [0,0,0])
            Play_button = pygame.transform.scale(buttons, (Play_Text.get_width()+20,Play_Text.get_height()+20))
            game_display.blit(Play_button,(O.Screen_Width/2-Play_button.get_size()[0]/2,play_Height))
            Play_rect = pygame.Rect(O.Screen_Width/2-Play_button.get_size()[0]/2,play_Height,Play_button.get_width(),Play_button.get_height())
            game_display.blit(Play_Text,(O.Screen_Width/2-Play_Text.get_width()/2+2,play_Height+7))

        if not Muted:
            game_display.blit(Sound_icon[0],(0,O.Screen_Height-Sound_icon[0].get_height()))
            pygame.mixer.music.unpause()
        if Muted:
            game_display.blit(Sound_icon[1],(0,O.Screen_Height-Sound_icon[0].get_height()))
            pygame.mixer.music.pause()
        #Makes it so when you hit X it closes the Program
        for event in pygame.event.get():
            Char_Name.handle_event(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mute_rect.collidepoint(mos_pos) and Muted == False:
                    Muted = True
                    O.Muted = True
                elif mute_rect.collidepoint(mos_pos) and Muted == True:
                    Muted = False
                    O.Muted = False
                if  back_rect.collidepoint(mos_pos):
                    display = False
                    main_menu(First=False)
                if Left_rect.collidepoint(mos_pos):
                    if Warrior_Type == 1:
                        Warrior_Type = 3
                    else:
                        Warrior_Type -= 1
                if Right_rect.collidepoint(mos_pos):
                    if Warrior_Type == 3:
                        Warrior_Type = 1
                    else:
                        Warrior_Type += 1
                try:
                    if Play_rect.collidepoint(mos_pos):
                        display = False
                        Characters_Name = Char_Name.saved_text
                        Game_Start_Screen(str(Warrior_Type), Characters_Name)
                except:
                    pass
        
        if  back_rect.collidepoint(mos_pos) and sound_cooldown <= 0:
            on_hover_sound.play()
            sound_cooldown = 20
        if  back_rect.collidepoint(mos_pos):
            pygame.draw.rect(game_display,[255,255,255,1],back_rect,3)
        try:
            if  Play_rect.collidepoint(mos_pos) and sound_cooldown <= 0:
                on_hover_sound.play()
                sound_cooldown = 20
            if  Play_rect.collidepoint(mos_pos):
                pygame.draw.rect(game_display,[255,255,255,1],Play_rect,3)
        except:
            pass
        sound_cooldown -= 1
        Frame += 1
        pygame.display.update()
        clock.tick(O.Screen_Updates)
        Clouds_num += 1.5

#Game_Start_Screen
def Game_Start_Screen(Warrior, Name):
    display = True
    opacity = 0
    pygame.mixer.music.fadeout(1000)
    while display:
        if opacity > 170:
            opacity = 255
            Game_Text_Start(str(Warrior), Name)
        fade = pygame.Surface((O.Screen_Width, O.Screen_Height)).convert()
        fade.set_alpha(opacity)
        game_display.blit(fade,(0,0))
        pygame.display.update()
        clock.tick(O.Screen_Updates/2)
        opacity += 1

#Game Text Start

def Game_Text_Start(warrior, Name):
    display = True
    Char = 0
    while display:
        if Char == len(W.Good_Morning):
            Char = len(W.Good_Morning)
            Main_Loop(str(warrior), Name)
        else:
            pass
        text = Options_Lesser_Font.render(W.Good_Morning[:Char], True, (255,255,255))
        game_display.blit(text, (50,100))
        Char += 1
        pygame.display.update()
        clock.tick(O.Screen_Updates/8)

#pause Menu

def pause_menu():
    display = True
    Back_Height = 900
    Main_Height = 800
    while display:
        mos_pos = pygame.mouse.get_pos()
        #Paused Text
        Text_Title = Title_Text.render('Paused', True, [0,0,0])
        game_display.blit(Text_Title,(O.Screen_Width/2-Text_Title.get_width()/2, O.Screen_Height/6))
        #Back Button
        Back_Text = Goth_Font.render('Back', True, [0,0,0])
        back_button = pygame.transform.scale(buttons, (Back_Text.get_width()+20,Back_Text.get_height()+20))
        game_display.blit(back_button,(O.Screen_Width/2-back_button.get_size()[0]/2,Back_Height))
        back_rect = pygame.Rect(O.Screen_Width/2-back_button.get_size()[0]/2,Back_Height,back_button.get_width(),back_button.get_height())
        game_display.blit(Back_Text,(O.Screen_Width/2-Back_Text.get_width()/2+2,Back_Height+7))
        #Return To Main Menu
        Main_Text = Goth_Font.render('Main Menu', True, [0,0,0])
        Main_button = pygame.transform.scale(buttons, (Main_Text.get_width()+20,Main_Text.get_height()+20))
        game_display.blit(Main_button,(O.Screen_Width/2-Main_button.get_size()[0]/2,Main_Height))
        main_rect = pygame.Rect(O.Screen_Width/2-Main_button.get_size()[0]/2,Main_Height,Main_button.get_width(),Main_button.get_height())
        game_display.blit(Main_Text,(O.Screen_Width/2-Main_Text.get_width()/2+2,Main_Height+7))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(mos_pos):
                    display = False
                if main_rect.collidepoint(mos_pos):
                    display = False
                    all_sprites.empty()
                    Collidables.empty()
                    Decor.empty()
                    Base.clear()
                    main_menu(False) 




#Main Loop

def Main_Loop(Warrior_Type, Warrior_Name):
    Display = True
    Frame = 0
    #Game Loop
    map = Map('map.txt', 'decor.txt')
    for row, tiles in enumerate(map.data):
            for col, tile in enumerate(tiles):
                Base_Sprite(col*4, row*4)
    for row, tiles in enumerate(map.data):
            for col, tile in enumerate(tiles):
                if tile in S.Sprite_Dict:
                    New_Sprite(col, row, S.Sprite_Dict[tile]['name'], S.Sprite_Dict[tile]['Collidable'])
                if tile == 'P':
                    player = Player(col, row, Warrior_Type, Warrior_Name)
    for row, tiles in enumerate(map.ddata):
            for col, tile in enumerate(tiles):
                if tile in S.Decor_Dict:
                    if 'Event' in S.Decor_Dict[tile]:
                        New_Decor(col, row, S.Decor_Dict[tile]['name'], S.Decor_Dict[tile]['Collidable'], S.Decor_Dict[tile]['Event'])
                    New_Decor(col, row, S.Decor_Dict[tile]['name'], S.Decor_Dict[tile]['Collidable'])
    camera = Camera(map.width, map.height)
    while Display:
        if Frame > 29:
            Frame = 0
        #Makes it so when you hit X it closes the Program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        player.animate(Frame)
        screen_update(camera, player)
        Frame += 1
        clock.tick(O.Screen_Updates)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.vel.x = -player.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.vel.x = player.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.vel.y = -player.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.vel.y = player.speed
        if player.vel.x != 0 and player.vel.y != 0:
            player.vel *= 0.7071
        if keys[pygame.K_ESCAPE]:
            pause_menu()
        if keys[pygame.K_i]:
            inventory_open()
        if keys[pygame.K_p]:
            inventory.append(Sword(5, doa))





    


# create the game object
main_menu(True)