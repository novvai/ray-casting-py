import pyglet

class Wall():
    def __init__(self, x1,y1,x2,y2):
        self.a = [float(x1),float(y1)]
        self.b = [float(x2),float(y2)]


    def draw(self):
        return (pyglet.graphics.vertex_list(2,("v2f", self.a+self.b))).draw(pyglet.gl.GL_LINES)