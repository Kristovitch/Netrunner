# import card
# import players
import pygame


class Board:
    def __init__(self) -> None:
        # Get the display surface
        self.display_surface = pygame.display.get_surface()
        self.game_paused = False

    def create_board(self) -> None:
        pass
