import sys
import pygame
import functional.game as game
import ui.ui_card as ui_card
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
        self.card = ui_card.UI_Card(groups=pygame.sprite.Group(),
                                    left=176,
                                    top=134,
                                    width=100,
                                    height=150,
                                    background=SETTINGS.HAASBIOROID_BACKGROUND)
        self.card2 = ui_card.UI_Card(groups=pygame.sprite.Group(),
                                     left=400,
                                     top=134,
                                     width=100,
                                     height=150,
                                     background=SETTINGS.SHAPER_BACKGROUND)
        self.hand = [self.card, self.card2]

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
                        for i in self.hand:
                            i.pickup(event)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        for i in self.hand:
                            i.drop()

                elif event.type == pygame.MOUSEMOTION:
                    for i in self.hand:
                        i.move(event)

            self.screen.fill(SETTINGS.UI_BG_COLOUR)

            for i in self.hand:
                i.draw(self.screen)

            pygame.display.update()
            self.clock.tick(SETTINGS.FPS)


if __name__ == '__main__':
    netrunner = Netrunner()
    netrunner.run()
