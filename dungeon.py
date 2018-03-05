import numpy as np
import random

DUNGEON_SIZE = 40
def dig(m, x, y):
    try: m[x, y] = '.'
    except IndexError:
        return
def generate_level(maxrooms=10, minsize=5, maxsize=10, seed=None):
    random.seed(seed)
    level = np.array(['#'
        for x in range(DUNGEON_SIZE)
        for y in range(DUNGEON_SIZE)
        ])
    level.resize(40, 40)
    rooms = [
        (random.randint(1, DUNGEON_SIZE - 2),
         random.randint(1, DUNGEON_SIZE - 2))
        for i in range(maxrooms)
        ]
    for x, y in rooms:
        size = random.randint(minsize, maxsize)

        for dx in range(size):
            for dy in range(size):
                dig(level, x + dx, y + dy)
                dig(level, x - dx, y - dy)
    for x in range(50):
        level[x, 0] = '#'
        level[x, 49] = '#'
    for y in range(50):
        level[0, y] = '#'
        level[40-1, y] = '#'

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
