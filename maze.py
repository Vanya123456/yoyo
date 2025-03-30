#создай игру "Лабиринт"!
from pygame import *

#создай окно игры
window = display.set_mode((700,500))
display.set_caption('Dogonyalki')
#задай фон сцены
background = transform.scale(image.load("background.jpg"),(700, 500))
#создай 2 спрайта и размести их на сцене
game = True
#обработай событие «клик по кнопке "Закрыть окно"»
clock = time.Clock()
FPS = 60
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
win_height = 500
win_wid = 700
ki = mixer.Sound('kick.ogg')
font.init()
font = font.SysFont('Arial', 70)
win = font.render("You WIN!", True, (255, 215, 0))


class GameSprite(sprite.Sprite):
    def __init__(self, player_x, player_y, player_speed, player_image):   
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        
        window.blit(self.image,(self.rect.x,self.rect.y))
NASH = GameSprite(5, win_height - 80, 4, "hero.png")
'''NeNASH = GameSprite(5, win_wid + 80, 2, "cyborg.png")'''
NeNASH = GameSprite(win_wid - 75, 420, 2, "cyborg.png")
class enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_wid - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class player(GameSprite):
    def update(self):
        key_presed = key.get_pressed()
        if key_presed[K_UP] and self.rect.y > win_height - 500  :
            self.rect.y -= 10
        if key_presed[K_DOWN] and self.rect.y < win_height - 60 :
            self.rect.y += 10
        if key_presed[K_LEFT] and self.rect.x > 1:
            self.rect.x -= 10
        if key_presed[K_RIGHT] and self.rect.x < 635 :
            self.rect.x += 10
class wall(sprite.Sprite):
    def __init__(self, wall_x, wall_y, red, green, blue, height, width):
        super().__init__()
        self.red = red
        self.green = green
        self.blue = blue
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((red, green, blue))        
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))



finish = False
wall1 = wall(300, 0, 145,7, 190, 300, 20)
wall = wall(100, 100, 145,7, 190, 1000, 20)
NASH1 = player(5, win_height - 80, 4, "hero.png")
NeNASH1 = enemy(win_wid - 75, 300, 2, "cyborg.png")
wall.draw_wall()
win11 = GameSprite(5, win_height - 80, 4, "treasure.png")
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False    
    if finish != True:

        clock.tick(FPS)
        window.blit(background,(0,0))
        '''NASH.reset()
        NeNASH.reset()'''
        NASH1.reset()
        NASH1.update()
        NeNASH1.reset()
        NeNASH1.update()    
        wall.draw_wall()
        wall1.draw_wall()
        if sprite.collide_rect(NASH1, NeNASH1) or sprite.collide_rect(NASH1, wall) or sprite.collide_rect(NASH1, wall1):
            finish = True
            window.blit(win,(200,200))
            ki.play()


    

        display.update()