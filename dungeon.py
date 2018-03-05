import numpy as np
import random

def generate_level(maxrooms=10, minsize=5, maxsize=10, seed=None):
    random.seed(seed)
    level = np.array(['#' for x in range(50) for y in range(50)])
    level.resize(50, 50)
    rooms = [
        (random.randint(1, 48), random.randint(1, 48))
        for i in range(maxrooms)
        ]
    for x, y in rooms:
        size = random.randint(minsize, maxsize)

        for dx in range(size):
            for dy in range(size):
                level[(x + dx), (y + dy)] = '.'
                level[(x - dx) % 50, (y + dy) % 50] = '.'

    for x in range(50):
        level[x, 0] = '#'
        level[x, 49] = '#'
    for y in range(50):
        level[0, y] = '#'
        level[49, y] = '#'

    room_path = {

    }
    first = rooms.pop(random.randint(0, len(rooms) - 1))
    last = first
    while rooms:
        room_path[last] = rooms.pop(random.randint(0, len(rooms) - 1))
        last = room_path[last]
    room_path[last] = first

    for k, v in room_path.items():
        x = k[0]
        y = k[1]
        while x < v[0]:
            level[x, y] = '.'
            x += 1
        while x > v[0]:
            level[x, y] = '.'
            x -= 1
        while y < v[1]:
            level[x, y] = '.'
            y += 1
        while y > v[1]:
            level[x, y] = '.'
            y -= 1
    return level
