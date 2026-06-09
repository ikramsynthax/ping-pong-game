from pygame import *
from random import randint

# --- INIT ---
init()
mixer.init()

mixer.music.load('chinesemusic.ogg')
mixer.music.play(-1)

# images
img_back = "background.jpg"
img_ball = "ball.png"
img_rod = "rod.png"

# background
win_width = 700
win_height = 500

# --- CLASSES ---
class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect(topleft=(x, y))

    def reset(self):
        window.blit(self.image, self.rect)

class Player(GameSprite):
    def update_l(self): 
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:  
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - self.rect.height:  
            self.rect.y += self.speed

    def update_r(self):  
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:  
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - self.rect.height:  
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, img, x, y, w, h, speed_x, speed_y):
        super().__init__(img, x, y, w, h, 0)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # Bounce off top/bottom
        if self.rect.y <= 0 or self.rect.y >= win_height - self.rect.height:
            self.speed_y *= -1

# --- OBJECTS ---
left_paddle = Player(img_rod, 30, win_height//2 - 60, 20, 120, 7)
right_paddle = Player(img_rod, win_width-50, win_height//2 - 60, 20, 120, 7)
ball = Ball(img_ball, win_width//2, win_height//2, 40, 40, 5, 5)

# --- WINDOW ---
display.set_caption("ping-pong game")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
