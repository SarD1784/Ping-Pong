from pygame import *
from random import randint

w=600
h=500
speed_x = 5
speed_y = 5
window = display.set_mode((w,h))
display.set_caption('Ping Pong')
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('Player 2 win!', True, (200,0,0))
lose2 = font1.render('Player 1 win!', True, (200,0,0))
class GameSprite(sprite.Sprite):
    def __init__(self, file, x, y, w, h, speed):
        super().__init__()
        self.image  = transform.scale(image.load(file), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player (GameSprite):
    def update1(self):
        k = key.get_pressed()
        if k[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if k[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update2(self):
        k = key.get_pressed()
        if k[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if k[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
p1=Player('rocket.png', 50,120,40,100,5)
p2=Player('rocket2.png', w-50,120,40,100,5)
ball=GameSprite('ball.png', 250,240,40,40,6)
background = transform.scale(image.load('fon.png'),(w,h))
game = True
finish = False
while game:
    window.blit(background,(0,0))
    if finish !=True:
            ball.rect.x += speed_x
            ball.rect.y += speed_y
    if sprite.collide_rect(p1, ball) or sprite.collide_rect(p2,ball):
        speed_x*=-1
    if ball.rect.y > h-50 or ball.rect.y < 0:
        speed_y*=-1
    if ball.rect.x < 5:
        finish = True
        window.blit(lose1, (w/2, h/2))
    if ball.rect.x > w-50:
        finish = True
        window.blit(lose2, (w/2, h/2))
    for e in event.get():
        if e.type == QUIT:
            game = False
    p1.reset()
    p2.reset()
    ball.reset()
    display.update()
    time.delay(50)
    p1.update1()
    p2.update2()