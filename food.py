import random


class Food:
    block_size = None
    color = (0, 255, 0)
    x = 0
    y = 0
    bounds = None

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds

    def draw(self, game, screen):
        game.draw.rect(screen, self.color, (self.x, self.y, self.block_size, self.block_size))

    def respawn(self):
        x_blocks = self.bounds[0] / self.block_size
        y_blocks = self.bounds[1] / self.block_size
        self.x = random.randint(0, x_blocks - 1) * self.block_size
        self.y = random.randint(0, y_blocks - 1) * self.block_size
