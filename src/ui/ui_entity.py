import pygame


class UI_Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pygame.math.Vector2()

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    # moving right
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    # moving left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    # moving down
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    # moving up
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
