import pyglet
import math
from pyglet.window import key
from wall import *
from entity import *
from slice import *
window = pyglet.window.Window(1600,800)
pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
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
"""frame"""
wall_arr += [Wall(1,1,1,799)]
wall_arr += [Wall(0,799,799,799)]
wall_arr += [Wall(799,799,799,1)]
wall_arr += [Wall(799,1,1,1)]

# initial position of all entities
entity_list = []
rays = 100
x1 = 400
y1 = 400
ws_arr = []
width = 799/rays
offset = width
position = 800+width/2
# ws = Slice(810,0,810,800,10)

for i in range(rays):
    angle = math.radians((i+1) / rays * -45)
    entity_list += [Entity(x1,y1, angle)]
    ws_arr+=[Slice(position,0,position,800,width, 800)]
    position+=offset

@window.event
def on_mouse_motion(x, y, dx, dy):
    for ent in entity_list:
            ent.pos[0] = x
            ent.pos[1] = y
@window.event        
def on_text_motion(symbol):
    ang = 0
    if symbol == key.MOTION_LEFT:
        ang = 1
    elif symbol == key.MOTION_RIGHT:
        ang = -1
    for ent in entity_list:
            ent.angle += math.radians(ang)


@window.event
def on_draw():
    window.clear()

    for w in wall_arr:
        w.draw()
    for index,ent in enumerate(entity_list):
        ent.castRays()
        for w in wall_arr:
            ent.check(w)

        dist = ent.get_distance()
        scale = 0
        # print(dist)
        if(dist<500 and dist>0):
            scale = dist
        ws_arr[index].scale_height_by(scale)
        ws_arr[index].draw()
        ent.draw()

if __name__ == "__main__":
    pyglet.app.run()