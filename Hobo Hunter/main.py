import pygame
import Options as O
import time
import random

try:
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
except:
    print('Pygame Failed to Initialize')

gamedisplay = pygame.display.set_mode((O.Screen_Width,O.Screen_Height))
font = pygame.font.SysFont('Engravers MT', 30)
clock = pygame.time.Clock()
pygame.display.set_caption('Combat Tester')
time_to_shoot = 0
time_to_shoot1 = 0
Projectiles = []
Enemies_List = []
Score = 0
Max_Enemies = 2
#LoadingImages

Background = pygame.image.load('Background.png')
FireBall = pygame.image.load('Fireball.png')
Char_Idle = [pygame.image.load('1.png'),pygame.image.load('2.png'),pygame.image.load('3.png'),pygame.image.load('4.png')]
Char_Attack =  [pygame.image.load('A1.png'),pygame.image.load('A2.png')]
Char_Right = [pygame.image.load('W1.png'),pygame.image.load('W2.png'),pygame.image.load('W3.png'),pygame.image.load('W4.png'),pygame.image.load('W5.png')]
Char_Left = [pygame.image.load('LW1.png'),pygame.image.load('LW2.png'),pygame.image.load('LW3.png'),pygame.image.load('LW4.png'),pygame.image.load('LW5.png')]
Char_Hit = [pygame.image.load('H1.png'),pygame.image.load('H2.png')]
Enemy_Idle = pygame.image.load('E1.png')
Enemy_Attack = [pygame.image.load('EA1.png'),pygame.image.load('EA2.png'),pygame.image.load('EA3.png'),pygame.image.load('EA4.png'),pygame.image.load('EA5.png')]
#LoadingSounds

Punch = pygame.mixer.Sound('Punch.wav')
Hit_Effect = pygame.mixer.Sound('Hit_Effect.wav')


class Player_Char():
    def __init__(self, x,y,health,damage):
        self.x = x
        self.y = y
        self.health = health
        self.damage = damage
        self.Direction = 'Idle'
        self.Visible = True
    def Draw(self, gamedisplay,Frame):
        if self.Visible:
            self.Health_Bar()
            if self.Direction == 'Idle':
                gamedisplay.blit(Char_Idle[Frame//5],(self.x,self.y))
            if self.Direction == 'Attack':
                Punch.play()
                gamedisplay.blit(Char_Attack[Frame//10],(self.x,self.y+15))
            if self.Direction == 'Right':
                gamedisplay.blit(Char_Right[Frame//4],(self.x,self.y))
            if self.Direction == 'Left':
                gamedisplay.blit(Char_Left[Frame//4],(self.x,self.y))
            if self.Direction == 'Damage':
                gamedisplay.blit(Char_Hit[Frame//10],(self.x,self.y))

    def Take_damage(self,damage):
        self.health -= damage
    def Heal(self,Healing):
        self.damage += Healing
    def Health_Bar(self):
        if self.Visible:
            if self.health > 100:
                self.health = 100
            if self.health <= 0:
                self.health = 0
                self.Die()
            pygame.draw.rect(gamedisplay, O.red, (self.x-10, self.y - 40, 100, 10))
            pygame.draw.rect(gamedisplay, O.black, (self.x-12, self.y - 42, 104, 14),3)
            pygame.draw.rect(gamedisplay, O.green, (self.x-10, self.y - 40, self.health, 10))
    def Die(self):
        self.Visible = False

        
class enemy():
    def __init__(self, x,y,health,damage):
        global Score
        self.x = x
        self.y = y
        self.health = health
        self.damage = damage
        self.direction = 'Idle'
        self.Visible = True
        self.Next_Hit = 0
    def Take_damage(self, damage):
        self.health -= damage
    def Heal(self,Healing):
        self.damage += Healing
    def Draw(self,gamedisplay,Frame):
        if self.Visible:
            self.Health_Bar()
            if self.direction == 'Idle':
                gamedisplay.blit(Enemy_Idle,(self.x,self.y))
            if self.direction == 'Attack':
                gamedisplay.blit(Enemy_Attack[Frame//4],(self.x,self.y))
    def Health_Bar(self):
        if self.Visible: 
            if self.health > 100:
                self.health = 100
            if self.health <= 0:
                self.health = 0
                self.Die()
            pygame.draw.rect(gamedisplay, O.red, (self.x-5, self.y - 20, 100, 10))
            pygame.draw.rect(gamedisplay, O.black, (self.x-6, self.y - 22, 104, 14),3)
            pygame.draw.rect(gamedisplay, O.green, (self.x-5, self.y - 20, self.health, 10))
    def Die(self):
        self.Visible = False
        global Score
        global Max_Enemies
        Score += 1
        Max_Enemies += 1
        


class Shoot():
    def __init__(self,x,y,speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.Visible = True
    def Draw(self, gamedisplay):
        self.Move()
        if self.Visible:
            gamedisplay.blit(FireBall,(self.x,self.y))
        if self.x > O.Screen_Width:
            self.Visible = False
            for i in Projectiles:
                if i == self:
                    Projectiles.remove(self)
        for Enemy in Enemies_List:
            if self.x > Enemy.x and self.x < Enemy.x + 50:
                Enemy.Take_damage(5)

    def Move(self):
        self.x += self.speed


def shoot():
    global time_to_shoot
    global time_to_shoot1
    time_to_shoot1 = time.strftime('%H,%M,%S')
    time_to_shoot1 = time_to_shoot1.replace(',', '', 2)

def reloa():
    global time_to_shoot
    
    time_to_shoot2 = time.strftime('%H,%M,%S')
    time_to_shoot2 = time_to_shoot2.replace(',', '', 2)
    time_to_shoot = int(time_to_shoot1) - int(time_to_shoot2)
def Enemy_Spawn():
    for i in range(Max_Enemies):
        Enemies_List.append(enemy(random.randint(1000,1200),O.Screen_Height-180,100,5))
def Redraw():
    global Frame
    global Next_Shot
    if Frame +1 >= 20:
        Frame = 0
    gamedisplay.blit(Background, (0,0))
    text = font.render('SCORE: ' + str(Score), 1,(220,220,220))
    gamedisplay.blit(text, (10,13))
    Player.Draw(gamedisplay,Frame)
    for g in Enemies_List:
        g.Next_Hit -= 1
        g.Draw(gamedisplay,Frame)
    for i in Projectiles:
        i.Draw(gamedisplay)
    Frame += 1
    #pygame.draw.rect(gamedisplay, O.red, (Player.x + 50, Player.y, 85, 143),1)
    #pygame.draw.rect(gamedisplay, O.green, (Enemy.x, Enemy.y, 143, 85))
    pygame.display.update()
    Next_Shot -= 1
    

clock.tick(20)
Frame = 0
Player = Player_Char(800,O.Screen_Height-180,100,5)
Next_Hit = 0
Next_Shot = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    Player.Direction = 'Idle'
    
    
    for g in Enemies_List:

        if g.Visible:
            if Player.x+20 < g.x:
                g.x -= 2
            if Player.x-20  > g.x:
                g.x += 2
            if Player.x < g.x and Player.x > g.x -50 and g.Next_Hit <= 0:
                g.direction = 'Attack'
                Player.Take_damage(g.damage)
                g.Next_Hit = 40
            if Player.x > g.x or Player.x < g.x -50:
                g.direction = 'Idle'
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and time_to_shoot < 0:
        shoot()
        Player.Direction = 'Attack'
        for Enemy in Enemies_List:
            if Enemy.x >= Player.x and Enemy.x <= Player.x+50:
                Enemy.Take_damage(Player.damage)
                Hit_Effect.play()
    
    if keys[pygame.K_d]:
        Player.Direction = 'Right'
        Player.x += 3
    
    if keys[pygame.K_a]:
        Player.Direction = 'Left'
        Player.x -= 3
    if keys[pygame.K_LEFT]:
        Player.health -= 2
    if keys[pygame.K_RIGHT]:
        Player.health += 2
    if keys[pygame.K_LCTRL] and Next_Shot <= 0 and Player.Visible:
        Projectiles.append(Shoot(Player.x,Player.y,20))
        Next_Shot = 40
    if Player.x <= 0:
        Player.x = 0
    if len(Enemies_List) < Max_Enemies:
        Enemy_Spawn()
    reloa()
    Redraw()

    