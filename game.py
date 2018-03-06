import dungeon
import tdl
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

con = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="MonkeyRL", fullscreen=False)

def printf(console, string, x=0, y=dungeon.DUNGEON_SIZE+1):
    for c in string:
        console.draw_char(x, y, c)
        x += 1
        if x >= SCREEN_WIDTH:
            y += 1
            x = 0
    while x < SCREEN_WIDTH:
        console.draw_char(x, y, ' ')
        x += 1
map_ = dungeon.generate_level()
print("Map generated.")

while not tdl.event.is_window_closed():
    for y, row in enumerate(map_.walkable):
        for x, column in enumerate(row):
            con.draw_char(x, y, '.' if column else '#')
    user_input = tdl.event.key_wait()
    x = 0
    y = 50
    printf(con, "Hello world!")
    if user_input.keychar == 'R':
        map_ = dungeon.generate_level()
    tdl.flush()
