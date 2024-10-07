import sys
import pygame
import settings as SETTINGS


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SETTINGS.WIDTH,
                                               SETTINGS.HEIGHT))
        pygame.display.set_caption('Netrunner')
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    print('keydown')
                    if event.key == pygame.K_m:
                        pygame.Rect(10, 10, SETTINGS.HEALTH_BAR_WIDTH,
                                    SETTINGS.BAR_HEIGHT)

            self.screen.fill(SETTINGS.UI_BG_COLOUR)
            pygame.display.update()
            self.clock.tick(SETTINGS.FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
