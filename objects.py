class GameObject:
    def __init__(self, tile, x, y, entities):
        self.tile = tile
        self.x = x
        self.y = y
        self.entities = entities
    def pos(self):
        return (self.x, self.y)

    def move(self, dx, dy):
        del self.entities[self.pos()]
        self.x += dx
        self.y += dy
        if self.pos() in entities:
            entities[self.pos()].on_collide(self, dx, dy)

class Character(GameObject):
    def __init__(self, tile, x, y, health, attack, armor, entities):
        self.tile = tile
        self.x = x
        self.y = y
        self.health = health
        self.attack = attack
        self.entities = entities
        self.armor = armor

    dead = False

    def damage(attack):
        self.health -= (attack - self.armor)
        if self.health == 0:
            self.dead = True

    def move(self, dx, dy):
        del self.entities[self.pos()]
        self.x += dx
        self.y += dy
        if self.pos() in entities:
            self.entities[self.pos()].on_collide(self, dx, dy)

    def on_collide(self, collider, dx, dy):
            self.damage(collider.attack)
            if self.dead:
                self.entities[collider.pos()] = collider
            else:
                collider.move(-dx, -dy)
                self.entities[oldx, oldy] = collider
