import uuid
from typing import Any
from typing import Dict
from typing import Optional

import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(
        self,
        uuid: str = uuid.uuid4(),
        x: int = 0,
        y: int = 0,
        action: str = "standard",
        direction: str = "down",
        index: int = 0,
        parent: Optional[Any] = None,
    ) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.uuid = uuid
        self.width = 64
        self.height = 64
        self.x = x
        self.y = y
        self.action = action
        self.direction = direction
        self.index = index
        self.parent = parent
        self.load_images()

    def load_images(self) -> None:
        self.images: Dict[str, pygame.image]
        self.images = {}
        name = self.__class__.__name__.lower().replace("sprite", "")
        for action in self.actions:
            self.images[action] = {}
            for direction in self.directions:
                self.images[action][direction] = []
                for index in [1, 2, 3, 4, 5, 6, 7, 8]:
                    try:
                        image = (
                            "images/"
                            + name
                            + "/"
                            + action
                            + "/"
                            + direction
                            + "/"
                            + str(index)
                            + ".png"
                        )
                        self.images[action][direction].append(pygame.image.load(image))
                    except:
                        None
                    else:
                        None

    def update(self) -> None:
        images = self.images[self.action][self.direction]
        self.index += 1
        if self.index >= len(images):
            self.index = 0
        self.set_image(images[self.index])

    def move(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def set_image(self, image: pygame.image) -> None:
        self.image = image
        size = self.image.get_rect().size
        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])
        # if self.direction == 'down':
        #     self.rect.midtop = (self.x, self.y)
        # elif self.direction == 'right':
        #     self.rect.midleft = (self.x, self.y)
        # elif self.direction == 'top':
        #     self.rect.midbottom = (self.x, self.y)
        # elif self.direction == 'left':
        #     self.rect.midright = (self.x, self.y)
        self.rect.center = (self.x, self.y)
        # self.image.rect.center = (self.x, self.y)
        # print(self.image.get_size())
        self.mask = pygame.mask.from_surface(self.image)
