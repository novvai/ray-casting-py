import pyglet
import math

class Slice():
    def __init__(self, x1,y1,x2,y2, tickness,height=800):
        self.height = height
        self.middle = height/2
        self.color_scale_facotr = 255/self.middle
        self.opacity = 255
        self.a = [float(x1-tickness/2),float(y1)]
        self.b = [float(x1-tickness/2),float(y2)]
        self.c = [float(x2+tickness/2),float(y2)]
        self.d = [float(x2+tickness/2),float(y1)]

    def scale_height_by(self,factor):
        height = (math.tan(45)*factor)/2
        calc_height = self.height-height
        self.opacity = calc_height*self.color_scale_facotr if calc_height>= self.middle and height!=0 else 0

        self.b[1] = calc_height if calc_height>= self.middle and height!=0 else 0
        self.c[1] = calc_height if calc_height>= self.middle and height!=0 else 0
        self.a[1] = height if height<= self.middle and height!=0 else 0  
        self.d[1] = height if height<= self.middle and height!=0 else 0  

        

    def draw(self):
        return (pyglet.graphics.vertex_list(4,
        ("v2f", self.a+self.b+self.c+self.d),
        ('c4B', (
            163, 11, 11 ,int(self.opacity),
            163, 11, 11 ,int(self.opacity),
            163, 11, 11 ,int(self.opacity),
            163, 11, 11 ,int(self.opacity)
            ))
        )).draw(pyglet.gl.GL_QUADS)