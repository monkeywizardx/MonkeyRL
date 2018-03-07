import random
def get_spawn_location(level, center, walk_dist=100):
    steps = (-1, 0, 1)
    x, y = center
    for dummy in range(100):
        dx = random.choice(steps)
        dy = random.choice(steps)
        if level.walkable[x + dx, y + dy]:
            x, y += dx, dy
