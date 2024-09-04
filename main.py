#pgzero
import random

TITLE = "Spaceship Shooter"
FPS = 30
HEIGHT = 400
WIDTH = 600

uzay = Actor('uzay')
gemi = Actor('gemi', (300, 300))

dusmanlar = []

for i in range(5): # 0 1 2 3 4
    x = random.randint(0, 600)
    y = random.randint(-400, -100)
    dusman = Actor("düşman", (x, y))
    dusman.speed = random.randint(4, 10)
    dusmanlar.append(dusman)
    
    
def dusman_gemisi():
    for i in range(len(dusmanlar)):
        if dusmanlar[i].y < 400:
            dusmanlar[i].y += dusmanlar[i].speed
        else:
            dusmanlar[i].x = random.randint(0, 600)
            dusmanlar[i].y = random.randint(-400, -100)
            dusmanlar[i].speed = random.randint(4, 10)
            
        if gemi.x > dusmanlar[i].x:
            dusmanlar[i].x += 2
        else:
            dusmanlar[i].x -= 2
            
def update(dt):
    dusman_gemisi()
    
    for i in range(len(dusmanlar)):
        if gemi.colliderect(dusmanlar[i]):
            exit()
    
def draw():
    uzay.draw()
    gemi.draw()
    # screen.draw.text('Uzay Yolculuğu', center=(300, 150), color="white", fontsize=36)
    
    for i in range(len(dusmanlar)):
        dusmanlar[i].draw()

def on_mouse_move(pos):
    gemi.pos = pos
    
