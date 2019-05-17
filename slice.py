import pyglet

class Slice():
    def __init__(self, x1,y1,x2,y2, tickness,height=None):
        self.a = [float(x1-tickness/2),float(y1)]
        self.b = [float(x1-tickness/2),float(y2)]
        self.c = [float(x2+tickness/2),float(y2)]
        self.d = [float(x2+tickness/2),float(y1)]



    def draw(self):
        return (pyglet.graphics.vertex_list(4,("v2f", self.a+self.b+self.c+self.d))).draw(pyglet.gl.GL_QUADS)
        # return (pyglet.graphics.vertex_list(4,("v2f", 
            # [800.,800.,800.,790.,810.,790.,810.,800.]
        # ))).draw(pyglet.gl.GL_QUADS)