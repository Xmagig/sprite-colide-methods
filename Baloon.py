import os
import random 
import pygame
class Settings:
    Window = pygame.rect.Rect(0,0,600,400)
    FPS = 60
    Timer = 0

    FILE_PATH = os.path.dirname(os.path.abspath(__file__))
    IMAGE_PATH = os.path.join(FILE_PATH,"images")
    Background = "background-01.png"
    black = (0,0,0)

class Bubble(pygame.sprite.Sprite):
    def __init__(self, x, y, withe=30, hight=30):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "Bubble.png"))
        self.image = pygame.transform.scale(self.image,(withe,hight))
        self.rect = self.image.get_rect()
        self.rect.topleft =(x,y)

class Obstakl(pygame.sprite.Sprite):
    def __init__(self, id,x, y, withe=30, hight=30,): # Id referes to The Obsticals apirance
        self.id = id
        super().__init__()
            #Square
        if self.id == 1:
            self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "Square.png"))
            self.image = pygame.transform.scale(self.image,(withe,hight))

            #Triangle
        elif self.id == 2:
            self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "Triangle.png")) 
            self.image = pygame.transform.scale(self.image,(withe,hight))

            #Circle
        elif self.id == 3:
            self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "Circle.png")) 
            self.image = pygame.transform.scale(self.image,(withe,hight))
            
            #Hexagon
        elif self.id == 4:
            self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "Hexagon.png")) 
            self.image = pygame.transform.scale(self.image,(withe,hight))
        
            #Hammer
        elif self.id == 5:
            self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "Hammer.png")) 
            self.image = pygame.transform.scale(self.image,(withe,hight))
        
            #Cross
        elif self.id == 6:
            self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, "Cross.png")) 
            self.image = pygame.transform.scale(self.image,(withe,hight))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


def main():
    os.environ["SDL_VIDEO_WINDOW_POS"] = "10, 50"  
    pygame.init()


    screen = pygame.display.set_mode(Settings.Window.size)  #Gibt die Groesse die oben in settings angegeben ist ab.
    pygame.display.set_caption("Growing Bloon")          # Setzt den tietel der window 
    clock = pygame.time.Clock()

    #obsticals = pygame.sprite.Group()

    background_image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, Settings.Background)).convert()
    background_image = pygame.transform.scale(background_image,Settings.Window.size)                        # Setzt den hintergrund auf die window size


    square_1 = Obstakl(id=1,x=300 ,y=200)
    square_2 = Obstakl(id=1,x=200 ,y=300)
    circle_1 = Obstakl(id=3,x=100,y= 50)
    circle_2 = Obstakl(id=3,x=125,y= 100)
    hammer_1 = Obstakl(id=5,x=550,y= 100)
    hammer_2 = Obstakl(id=5,x=100,y= 350)

    bubble = Bubble(100,100)

    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        screen.blit(background_image,(0,0))
        #screen.fill(Settings.black)
        
        withe_buble = bubble.image.get_width()
        hight_buble = bubble.image.get_height()
        bubble.image = pygame.transform.scale(bubble.image, (withe_buble+1, hight_buble+1))




        screen.blit(bubble.image, bubble.rect)
        screen.blit(square_1.image, square_1.rect)
        screen.blit(square_2.image, square_2.rect)
        screen.blit(circle_1.image, circle_1.rect)
        screen.blit(circle_2.image, circle_2.rect)
        screen.blit(hammer_1.image, hammer_1.rect)
        screen.blit(hammer_2.image, hammer_2.rect)
        

        pygame.display.flip()

        Settings.Timer+=1   
        if Settings.Timer == 30:
            Settings.Timer=0
        clock.tick(Settings.FPS)

    pygame.quit()

if __name__ == "__main__":
    main()