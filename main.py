import pyglet
import math
from wall import *
from entity import *
from slice import *
window = pyglet.window.Window(1600,800)

# building all walls 
wall_arr = []
wall_arr += [Wall(100,250,150,150)]
wall_arr += [Wall(210,480,390,510)]
wall_arr += [Wall(150,150,50,50)]
wall_arr += [Wall(250,340,260,390)]
wall_arr += [Wall(260,390,210,480)]
wall_arr += [Wall(50,50,100,250)]

wall_arr += [Wall(450,450,250,340)]
wall_arr += [Wall(390,510, 375,800)]
wall_arr += [Wall(1,1,1,799)]
wall_arr += [Wall(0,799,799,799)]
wall_arr += [Wall(799,799,799,1)]
wall_arr += [Wall(799,1,1,1)]

# initial position of all entities
entity_list = []
rays = 10
x1 = 400
y1 = 400
ws_arr = []
width = 799/rays
offset = width+1
position = 800+width/2
# ws = Slice(810,0,810,800,10)

for i in range(rays):
    angle = math.radians((i+1) / rays * -45)
    entity_list += [Entity(x1,y1, angle)]
    ws_arr+=[Slice(position,0,position,800,width)]
    position+=offset

@window.event
def on_mouse_motion(x, y, dx, dy):
    for ent in entity_list:
            ent.pos[0] = x
            ent.pos[1] = y



@window.event
def on_draw():
    window.clear()

    for w in wall_arr:
        w.draw()
    for ent in entity_list:
        ent.castRays()
        for w in wall_arr:
            ent.check(w)

        ent.draw()
    for sl in ws_arr:
        sl.draw()



if __name__ == "__main__":
    pyglet.app.run()