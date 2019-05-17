import pyglet
import math

class Entity():
    def __init__(self,x,y, angle):
        self.pos = [x,y]
        self.angle = angle
        self.dir = []

    def draw(self):
        return (pyglet.graphics.vertex_list(2,("v2f", self.pos+self.dir),('c3B', (125, 122, 0, 100, 100, 0)))).draw(pyglet.gl.GL_LINES)
    
    # cast a ray in a given direction
    def castRays(self):
        x1 = math.cos(self.angle)*9999 + self.pos[0]
        y1 = math.sin(self.angle)*9999 + self.pos[1]
        self.dir = [x1,y1]

    # check if the ray has intersect a wall
    # true -> changes the dir vector to intersection points
    def check(self, wall):
        t1 = (self.pos[0] - wall.a[0])*(wall.a[1]-wall.b[1]) - (self.pos[1]-wall.a[1])*(wall.a[0]-wall.b[0]) 
        u1 = (self.pos[0]-self.dir[0])*(self.pos[1]-wall.a[1])-(self.pos[1]-self.dir[1])*((self.pos[0]-wall.a[0]))
        denominator = (self.pos[0] - self.dir[0])*(wall.a[1]-wall.b[1]) - (self.pos[1]-self.dir[1])*(wall.a[0]-wall.b[0])
        if denominator == 0:
            return None
        
        u = -(u1/denominator)
        t = t1/denominator

        lines_intersect = (0 <= u and u <=1) and (0<=t and t <= 1)

        if lines_intersect:
            self.dir[0] = self.pos[0]+t*(self.dir[0]-self.pos[0])
            self.dir[1] = self.pos[1]+t*(self.dir[1]-self.pos[1])




        