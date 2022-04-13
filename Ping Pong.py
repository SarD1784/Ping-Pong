from pygame import *
from random import randint

w=600
h=500
window = display.set_mode((w,h))
display.set_caption('Ping Pong')
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
        if k[K_s] and self.rect.y > 0:
            self.rect.y += self.speed
        if k[K_w] and self.rect.y < 700-30:
            self.rect.y -= self.speed
    def update2(self):
        k = key.get_pressed()
        if k[K_DOWN] and self.rect.y > 0:
            self.rect.y += self.speed
        if k[K_UP] and self.rect.y < 700-30:
            self.rect.y -= self.speed
p1=Player('rocket.png', 50,120,40,100,5)
p2=Player('rocket2.png', w-50,120,40,100,5)
p3=GameSprite('ball.png', 250,240,40,40,6)
background = transform.scale(image.load('fon.png'),(w,h))
game = True
while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    p1.reset()
    p2.reset()
    p3.reset()
    display.update()
    time.delay(50)
    p1.update1()
    p2.update2()