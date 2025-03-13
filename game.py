import pygame

import sys

#game class for object 'Game'
class Game:
    def __init__(self):

        pygame.init()

        pygame.display.set_caption('Escape the Night')

        self.screen = pygame.display.set_mode((1000, 640))

        self.clock = pygame.time.Clock()
        self.image =pygame.image.load('level background/simplified/Level_0/Decor.png')
        self.image = pygame.image.load('level background/ simplified/Level_0/Fence.png')

        self.image_pos = [0,0]

    def run(self):
        while True:
            self.screen.blit(self.image,self.image_pos)

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        
            pygame.display.update()
            self.clock.tick(60)

Game().run()

