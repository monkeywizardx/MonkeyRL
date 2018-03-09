class EntityLookup:
    self.lookup = {

    }

    def act(self, x, y):
        if (x, y) not in self.lookup:
            no_entity(x, y)

        self.lookup[x, y].act(self, x, y)

    def no_entity(self, x, y):
        raise ValueError("No entity at ({x}, {y})".format(x=x, y=y))

    def move_entity(self, cx, cy, dx, dy):
        if (cx, cy) not in self.lookup:
            raise ValueError("No entity at ({x}, {y})".format(x=cx, y=cy))

        entity = self.lookup[cx, cy]
        if (cx+dx, cy+dy) in self.lookup:
            self.lookup[dx, dy].on_collide(self, entity, dx, dy)
        else:
            del self.lookup[cx, cy]
            self.lookup[dx, dy] = entity

    def draw_entity(self, con, x, y):
        t = self.lookup[x, y]
        con.draw_char(x, y, t.tile, fg=t.fg, bg=t.bg)

class Entity:
    def __init__(self, tile, color=(255,255,255), bg=(0,0,0)):
        self.tile = tile
        self.fg = color
        self.bg = color

    def act(self, positions, x, y):
        return NotImplemented

    def on_collide(self, positions, entity, dx, dy):
        return NotImplemented

class Tile(Entity):
    def on_collide(self, positions, entity, dx, dy):
        "Do nothing."
        pass

    def act(self, positions, x, y):
        pass
