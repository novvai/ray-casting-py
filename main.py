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
"""frame"""
wall_arr += [Wall(1,1,1,799)]
wall_arr += [Wall(0,799,799,799)]
wall_arr += [Wall(799,799,799,1)]
wall_arr += [Wall(799,1,1,1)]

# initial position of all entities
entity_list = []
rays = 150
x1 = 400
y1 = 400
ws_arr = []
width = 799/rays
offset = width
position = 800+width/2
# ws = Slice(810,0,810,800,10)

edit_mode=[False]
wall_buffer = []

for i in range(rays):
    angle = math.radians((i+1) / rays * 45)
    entity_list += [Entity(x1,y1, angle)]
    ws_arr+=[Slice(position,0,position,800,width, 800)]
    position+=offset

def save_map(coords):
    file_wr = open("map.csv", "w+")
    for coord in coords:
        file_wr.write(coord.get_coords() + " \n")
    file_wr.close()

def load_map(coords):
    file_wr = open("map.csv", "r")
    coords.clear()
    file_lines = file_wr.readlines()
    for line in file_lines:
        x,y,x1,y1 = line.split(',')
        coords.append(Wall(x,y,x1,y1))

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT and edit_mode[0]:
        wall_buffer.append([x,y])
        print(wall_buffer, len(wall_buffer))
        if len(wall_buffer) == 2:
            wall_arr.append(Wall(wall_buffer[0][0],wall_buffer[0][1],wall_buffer[1][0],wall_buffer[1][1]))
            wall_buffer.clear()

@window.event
def on_mouse_motion(x, y, dx, dy):
    if edit_mode[0] == False:
        for ent in entity_list:
                ent.pos[0] = x
                ent.pos[1] = y

@window.event
def on_key_press(symbol, modifiers):
    # print(key.E , key.MOD_SHIFT)
    print(symbol , modifiers)
    if symbol == key.E and modifiers == 17:
        edit_mode[0] = False if edit_mode[0] else True
    if symbol == key.S and modifiers == 18:
        save_map(wall_arr)
    if symbol == key.D and modifiers == 18:
        load_map(wall_arr)

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