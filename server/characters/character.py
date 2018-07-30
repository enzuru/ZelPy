import pygame
from directories.sprite_directory import SpriteDirectory


class Character:

    def move(self, x, y):
        update = True
        self.sprite.move(x, y)
        collisions = pygame.sprite.spritecollide(self.sprite, SpriteDirectory.sprite_group, False, pygame.sprite.collide_mask)
        print(collisions)
        for sprite in collisions:
            if sprite is not self.sprite:
                update = False
        if update is True:
            self.x = x
            self.y = y
        else:
            self.sprite.move(self.x, self.y)


    def right(self):
        self.move(self.x + 1, self.y)

    def left(self):
        self.move(self.x - 1, self.y)

    def up(self):
        self.move(self.x, self.y - 1)

    def down(self):
        self.move(self.x, self.y + 1)
