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
        self.running = False

        # Set up game objects
        self.game = game.Game()
        self.game.setup('runner_deck', 'corp_deck')

        # Test Objects
        self.rectangle = pygame.rect.Rect(176, 134, 17, 17)
        self.rectangle_draging = False

    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    print('keydown')
                    if event.key == pygame.K_1:
                        self.game.next_turn(self.game.corp)
                    if event.key == pygame.K_2:
                        self.game.next_turn(self.game.runner)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.rectangle.collidepoint(event.pos):
                            self.rectangle_draging = True
                            mouse_x, mouse_y = event.pos
                            offset_x = self.rectangle.x - mouse_x
                            offset_y = self.rectangle.y - mouse_y
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.rectangle_draging = False

                elif event.type == pygame.MOUSEMOTION:
                    if self.rectangle_draging:
                        mouse_x, mouse_y = event.pos
                        self.rectangle.x = mouse_x + offset_x
                        self.rectangle.y = mouse_y + offset_y

            self.screen.fill(SETTINGS.UI_BG_COLOUR)
            pygame.draw.rect(self.screen,
                             SETTINGS.HAASBIROID_BACKGROUND,
                             self.rectangle)
            pygame.display.update()
            self.clock.tick(SETTINGS.FPS)


if __name__ == '__main__':
    netrunner = Netrunner()
    netrunner.run()
