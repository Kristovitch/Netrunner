import sys
import pygame
import game
import settings as SETTINGS


class Netrunner:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SETTINGS.WIDTH,
                                               SETTINGS.HEIGHT))
        pygame.display.set_caption('Netrunner')
        self.clock = pygame.time.Clock()

        self.game = game.Game()
        self.game.setup('runner_deck', 'corp_deck')

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    print('keydown')
                    if event.key == pygame.K_1:
                        self.game.next_turn(self.game.corp)
                    if event.key == pygame.K_2:
                        self.game.next_turn(self.game.runner)

            self.screen.fill(SETTINGS.UI_BG_COLOUR)
            pygame.display.update()
            self.clock.tick(SETTINGS.FPS)


if __name__ == '__main__':
    netrunner = Netrunner()
    netrunner.run()
