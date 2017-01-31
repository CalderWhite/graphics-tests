import pygame, os, json, math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
class util(object):
    class generate(object):
        def rect_prism(name,start_point,wlh):
            w, l, h = wlh
            x,y,z = start_point
            gen = {
                "id" : name,
                "points" : [
                [x,y-h,z], # bottom layer
                [x,y-h,z + l],
                [x + w,y-h,z+l],
                [x+w,y-h,z], # now top layer
                [x,y,z],
                [x,y,z + l],
                [x + w,y,z+l],
                [x+w,y,z]
                ],
                "lines" : [
                    [0,1], # bottom side edges
                    [1,2],
                    [2,3],
                    [3,0],
                    [4,5], # top side edges
                    [5,6],
                    [6,7],
                    [7,4],
                    [0,4], # height edges
                    [1,5],
                    [2,6],
                    [3,7]
                ]
            }
            return gen
        def lined_rect_prism(name,start_point,wlh,line_rate=1.5):
            w, l, h = wlh
            x,y,z = start_point
            # w : x
            # h : y
            # l : z
            # gen is the basic outline of a rectangle
            gen = {
                "id" : name,
                "points" : [
                [x,y-h,z], # bottom layer
                [x,y-h,z + l],
                [x + w,y-h,z+l],
                [x+w,y-h,z], # now top layer
                [x,y,z],
                [x,y,z + l],
                [x + w,y,z+l],
                [x+w,y,z]
                ],
                "lines" : [
                    [0,1], # bottom side edges
                    [1,2],
                    [2,3],
                    [3,0],
                    [4,5], # top side edges
                    [5,6],
                    [6,7],
                    [7,4],
                    [0,4], # height edges
                    [1,5],
                    [2,6],
                    [3,7]
                ]
            }
            # firstly width wise
            for i in range(1,math.floor(w/line_rate)):
                m = i * line_rate
                gp1 = [
                    x + m,
                    y,
                    z
                ]
                gp2 = [
                    x + m,
                    y,
                    z + l
                ]
                gen["points"].append(gp1)
                gen["points"].append(gp2)
                gen["lines"].append(
                    [len(gen["points"]) - 2,len(gen["points"]) - 1]
                )
            # secondly length wise
            for i in range(1,math.floor(w/line_rate)):
                m = i * line_rate
                gp1 = [
                    x,
                    y,
                    z + m
                ]
                gp2 = [
                    x + w,
                    y,
                    z + m
                ]
                gen["points"].append(gp1)
                gen["points"].append(gp2)
                gen["lines"].append(
                    [len(gen["points"]) - 2,len(gen["points"]) - 1]
                )
            # left side
            for i in range(1,math.floor(w/line_rate)):
                m = i * line_rate
                gp1 = [
                    x + m,
                    y,
                    z
                ]
                gp2 = [
                    x + m,
                    y - h,
                    z
                ]
                gen["points"].append(gp1)
                gen["points"].append(gp2)
                gen["lines"].append(
                    [len(gen["points"]) - 2,len(gen["points"]) - 1]
                )
            # left side across
            for i in range(1,math.floor(w/line_rate)):
                m = i * line_rate
                gp1 = [
                    x,
                    y - m,
                    z
                ]
                gp2 = [
                    x + w,
                    y - m,
                    z
                ]
                gen["points"].append(gp1)
                gen["points"].append(gp2)
                gen["lines"].append(
                    [len(gen["points"]) - 2,len(gen["points"]) - 1]
                )
            return gen
class event_handler(object):
    def __init__(self,triggers):
        self.triggers = triggers
    def update(self):
        for event in pygame.event.get():
            for e in self.triggers:
                if event.type == e:
                    self.triggers[e](event)
class window_manager(object):
    def __init__(self,name,dimensions,stop,motion,check_keys):
        # actual graphics
        pygame.display.set_mode(dimensions, DOUBLEBUF|OPENGL)
        pygame.display.set_caption(name)
        gluPerspective(45, (dimensions[0]/dimensions[1]), 0.1, 50.0)
        # events
        tl = {
            pygame.QUIT : stop,
            pygame.MOUSEMOTION : motion,
            pygame.KEYDOWN : check_keys
        }
        self.events = event_handler(tl)
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(1)
    def p(self,*args,**kwargs):
        pass
class shape_manager(object):
    def __init__(self,load="*",worlds_dir="./worlds"):
        self.worlds = {}
        # the selecting
        if load == "*":
            l = os.listdir(worlds_dir)
        else:
            l = [load]
        # the actual loadings
        if l.__contains__("Thumbs.db"):
            l.pop(l.index("Thumbs.db"))
        for f in l:
            try:
                r = open(worlds_dir + "/" + f,'r').read()
                j = json.loads(r)
                self.worlds[f] = j
            except ValueError:
                8("There was a formatting error [%s], therefore it will not be used." % f)
        self.current_world = {"shapes":[],"name":"<EMPTY>"}
        self.objects = []
    def add_object(self,obj):
        self.objects.append(obj)
    def select_world(self,name):
        for i in self.worlds:
            try:
                if self.worlds[i]["name"] == name:
                    self.current_world = self.worlds[i]
                    return True
            except KeyError:
                print("Error. [%s] worlds file doesn't have a name property.")
        return False
class Camera(object):
    def __init__(self):
        self.pos = [0,0,0]
        self.rot = [0,0]
class gfx_engine(object):
    def __init__(self,use_mouse=True):
        # properties
        self.looping = False
        self.shapes_manager = shape_manager()
        self.shapes_manager.select_world("myworld.json")
        self.camera = Camera()
        # testing values
        if use_mouse:
            mf = self.capture_mouse
        else:
            mf = self.p
        # window manager (includes testing value "mf")
        self.manager = window_manager(
            "e world",
            [640,480],
            self.stop,
            mf,
            self.key_bindings
        )
        # adding test shapes to the manager
        j = util.generate.rect_prism("cube",[3,0,0],[1,1,1])
        j1 = util.generate.rect_prism("cube2",[-3,0,0],[1,1,1])
        self.shapes_manager.add_object(util.generate.rect_prism("x",[0,0,0],[0,0,3]))
        self.shapes_manager.add_object(j)
        self.shapes_manager.add_object(j1)
    def stop(self,event):
        self.looping = False
        pygame.quit()
    def p(self,*args,**kwargs):
        """passing function for the sake of not doing anything.... yup..."""
        pass
    def key_bindings(self,event):
        if event.key == pygame.K_ESCAPE:
            self.stop(None)
    def draw(self,d):
        glBegin(GL_LINES)
        for line in d["lines"]:
            for point in line:
                glVertex3fv(d["points"][point])
        glEnd()
    def render_all(self):
        for shape in self.shapes_manager.current_world["shapes"]:
            self.draw(shape)
        for shape in self.shapes_manager.objects:
            self.draw(shape)
    def capture_mouse(self,event):
        x,y = event.rel
        x/=8;y/=8
        self.camera.rot[0]+=x;
        self.camera.rot[1]+=y;
    def check_keys(self):
        """Please don't mess with this function.... just don't"""
        speed = 1 / 50
        keys = pygame.key.get_pressed()
        # self.cc converts it to a different sytem which I wrote this equation for
        x,z = speed * math.sin(self.cc(self.camera.rot[0])),speed*math.cos(self.cc(self.camera.rot[0]))
        x*=-1
        ##print([float(str(x)[:5]),float(str(z)[:5])],self.camera.rot)
        # keysss
        if keys[pygame.K_w]:self.camera.pos[0]+=x;self.camera.pos[2]+=z
        if keys[pygame.K_s]:self.camera.pos[0]-=x;self.camera.pos[2]-=z
        if keys[pygame.K_d]:self.camera.pos[0]-=z;self.camera.pos[2]+=x
        if keys[pygame.K_a]:self.camera.pos[0]+=z;self.camera.pos[2]-=x
        if keys[pygame.K_SPACE]:self.camera.pos[1]-=speed
        if keys[pygame.K_LSHIFT]:self.camera.pos[1]+=speed
        if keys[pygame.K_e]:self.camera.rot[0]+=speed*100
        if keys[pygame.K_q]:self.camera.rot[0]-=speed*100
    def cc(self,num):
        """self.cc converts it to a different sytem which I wrote the movement equation for."""
        return num/ 100 * (6/3.6)
    def run(self):
        self.looping = True
        self.camera.pos = [0,0,-5]
        while self.looping:
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            w,h = pygame.display.get_surface().get_size()
            self.check_keys()
            # clear all transformations
            glLoadIdentity()
            # set perspective, since it is also reset when Identity is loaded
            gluPerspective(45, (w/h), 0.1, 50.0)
            # set viewing angle
            # -ALWAYS rotate along the xy axis first
            glRotatef(self.camera.rot[1],1,0,0)
            # then the xz axis
            glRotatef(self.camera.rot[0],0,1,0)
            # move world according to camera's position
            camx,camy,camz = self.camera.pos
            glTranslatef(camx,camy,camz)
            # render all points
            self.render_all()
            # update pygame display.
            pygame.display.flip()
            # fps stuff
            pygame.time.wait(10)
            # update events lastly, to avoid quitting errors
            self.manager.events.update()
if __name__ == '__main__':
    engine = gfx_engine()
    engine.run()