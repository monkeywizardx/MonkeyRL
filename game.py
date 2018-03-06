import dungeon
import tdl
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

con = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="MonkeyRL", fullscreen=False)
map_ = dungeon.generate_level()
print("Map generated.")

while not tdl.event.is_window_closed():
    for y, row in enumerate(map_.walkable):
        for x, column in enumerate(row):
            con.draw_char(x, y, '.' if column else '#')
    tdl.flush()
