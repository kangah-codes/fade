import pygame

#screen = pygame.display.set_mode((600, 500))
pygame.init()

class FadingText():
    def __init__(self, text, color, size, fadespeed):
        self.text = text
        self.color = color
        self.size = size
        self.speed = fadespeed
        self.font = pygame.font.Font("retro.ttf", self.size)
        self.font1 = pygame.font.Font("retro.ttf", 30)
        self.rendered = None
        self.alpha = 255

    def render(self):
        try:
            self.rendered = self.font.render(f"{self.text}", True, self.color)
        except:
            pass
        #screen.blit(self.rendered, (100,100))

    def fade(self, display, x, y):
        try:
            temp = pygame.Surface((self.rendered.get_width(), self.rendered.get_height())).convert()
            temp.blit(display, (-x,-y))
            temp.blit(self.rendered, (0,0))
            if self.alpha > 0:
                temp.set_alpha(self.alpha)
                self.alpha -= self.speed
                display.blit(temp, ((display.get_width()/2)-(temp.get_width()/2), y))
        except:
            pass
        

# f = FadingText("LOLS", [255,255,255], 32, 10)

# done = False

# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#             pygame.quit()

#     screen.fill((0,0,0))

#     f.render()
#     f.fade(screen)

#     pygame.display.update()




        # if self.pos.y < ball.pos.y and self.pos.y + self.rect.height > ball.pos.y + ball.rect.height:
        #         if ball.pos.x + ball.rect.width >= self.pos.x and ball.pos.x + ball.rect.width <= (self.pos.x+self.rect.width/2):
        #             ball.xspeed = -self.bounceSpeed
        #             self.kill()
        #         else:
        #             ball.xspeed = self.bounceSpeed
        #             self.kill()
        #     if self.pos.x < ball.pos.x and self.pos.x + self.rect.width > ball.pos.x + ball.rect.width:
        #         if ball.pos.y + ball.rect.height >= self.pos.y and self.pos.y + self.rect.height <= (self.pos.y + self.rect.height/2):
        #             ball.yspeed = -self.bounceSpeed
        #             self.kill()
        #         else: 
        #             ball.yspeed = self.bounceSpeed
        #             self.kill()
        