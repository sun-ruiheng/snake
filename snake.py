from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Snake():
    length = None
    direction = None
    body = None
    block_size = None
    color = (230, 230, 255)
    bounds = None

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds
        self.respawn()

    def respawn(self):
        self.length = 3
        self.body = [(20, 20), (20, 40), (20, 60)]
        self.direction = Direction.DOWN

    def draw(self, game, window):
        for block in self.body:
            game.draw.rect(window, self.color, (block[0], block[1], self.block_size, self.block_size))

    def move(self):
        cur_head = self.body[-1]
        if self.direction == Direction.UP:
            new_head = (cur_head[0], cur_head[1] - self.block_size)
            self.body.append(new_head)
        elif self.direction == Direction.DOWN:
            new_head = (cur_head[0], cur_head[1] + self.block_size)
            self.body.append(new_head)
        elif self.direction == Direction.LEFT:
            new_head = (cur_head[0] - self.block_size, cur_head[1])
            self.body.append(new_head)
        elif self.direction == Direction.RIGHT:
            new_head = (cur_head[0] + self.block_size, cur_head[1])
            self.body.append(new_head)
        if self.length < len(self.body):
            self.body.pop(0)

    def steer(self, direction):
        if direction == Direction.UP and self.direction != Direction.DOWN:
            self.direction = direction
        elif direction == Direction.DOWN and self.direction != Direction.UP:
            self.direction = direction
        elif direction == Direction.LEFT and self.direction != Direction.RIGHT:
            self.direction = direction
        elif direction == Direction.RIGHT and self.direction != Direction.LEFT:
            self.direction = direction

    def eat(self):
        self.length += 1

    def check_for_food(self, food):
        head = self.body[-1]
        if head[0] == food.x and head[1] == food.y:
            self.eat()
            food.respawn()

    def check_tail_collision(self):
        head = self.body[-1]
        for seg in self.body[:-1]:
            if head[0] == seg[0] and head[1] == seg[1]:
                return True
        return False

    def check_bounds(self):
        head = self.body[-1]
        if head[0] >= self.bounds[0] or head[0] < 0 or head[1] >= self.bounds[1] or head[1] < 0:
            return True
        return False
