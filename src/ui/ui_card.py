import pygame
from ui.ui_entity import UI_Entity


class UI_Card(UI_Entity):
    def __init__(self,
                 groups: pygame.sprite.Group,
                 left: float | int,
                 top: float | int,
                 width: float | int,
                 height: float | int,
                 background: str) -> None:
        '''
        A class that handles all UI elements of a card.

        Parameters
        ----------
        groups: pygame.sprite.Group
            The sprite group that the Card belongs to.

        left: float | int
            The position of the left edge of the card when spawned.

        top: float | int
            The position of the top edge of the card when spawned.

        width: float | int
            The width of the card when spawned.

        height: float | int
            The height of the card when spawned.

        background: str
            The background image for the card.

        Returns
        ----------
        None

        Raises
        ----------
        None
        '''
        super().__init__(groups)
        self.sprite_type = 'Card'
        self.left: float = left
        self.top: float = top
        self.height: float = height
        self.width: float = width
        self.offset_x = 0
        self.offset_y = 0
        self.background = background

        self.rectangle = pygame.rect.Rect(self.left, self.top, self.width, self.height)

        self.dragging = False

    def pickup(self, event: pygame.event) -> None:
        '''
        Pick up the card.

        Parameters
        ----------
        event: pygame.event
            The pygame event that will pick up the card
            Usually this should be MOUSEBUTTONDOWN

        Returns
        ----------
        None

        Raises
        ----------
        None
        '''
        if self.rectangle.collidepoint(event.pos):
            self.dragging = True
            mouse_x, mouse_y = event.pos
            self.offset_x = self.rectangle.x - mouse_x
            self.offset_y = self.rectangle.y - mouse_y

    def move(self, event: pygame.event) -> None:
        '''
        Move a card that is picked up.

        Parameters
        ----------
        event: pygame.event
            The pygame event that will move the card.
            Usually this should be MOUSEMOTION.

        Returns
        ----------
        None

        Raises
        ----------
        None
        '''
        if self.dragging:
            print('Moving')
            mouse_x, mouse_y = event.pos
            self.rectangle.x = mouse_x + self.offset_x
            self.rectangle.y = mouse_y + self.offset_y

    def drop(self):
        '''
        Drop a card that is picked up.

        Parameters
        ----------
        None

        Returns
        ----------
        None

        Raises
        ----------
        None
        '''
        self.dragging = False

    def import_graphics(self):
        '''
        Import and set up the graphical elements of a card.

        Parameters
        ----------
        None

        Returns
        ----------
        None

        Raises
        ----------
        None
        '''
        pass

    def draw(self, surface: pygame.surface.Surface):
        '''
        Draw the card on the screen

        Parameters
        ----------
        surface: pygame.surface.Surface
            The surface / screen that the card should be drawn on.

        Returns
        ----------
        None

        Raises
        ----------
        None
        '''
        pygame.draw.rect(surface, self.background, self.rectangle)
