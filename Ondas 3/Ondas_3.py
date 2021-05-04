import vpython as vp
from math import pi, ceil, sqrt


tela = vp.canvas(title='waves 3', width=800, height=600, center=vp.vector(0,0,0),
                 background=vp.color.white)
z = 0

class Wave:
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.waves = []
    def wave(self, rad, ang):
        self.rad = rad
        self.ang = ang
        onda = vp.shapes.arc(pos = [self.cx, self.cy], radius=rad, angle1=(pi-ang)/2, angle2=((pi + ang)/2))
        pathonda = [vp.vector(0, 0, z), vp.vector(0, 0, 0.01)]
        wv = vp.extrusion(path = pathonda, shape = onda, color = vp.color.black)
        self.waves.append(wv)
    def plain(self, lbd):
        self.lbd = lbd
        y0 = -20
        for w in range(ceil(20/lbd)):
            onda = vp.shapes.line(start=(-50,y0), end=(50,y0), np=20, thickness= 0.1)
            pathonda = [vp.vector(0, 0, z), vp.vector(0, 0, 0.01)]
            vp.extrusion(path = pathonda, shape = onda, color = vp.color.black)
            y0 += lbd
        
class Stilt:
    def __init__(self):
        pass
    def double_stilt(self, L, dl):
        self.L = L
        self.dl = dl
        x10 = (-L/2) - dl - 25
        xL = 50
        x20 = (L/2) + dl + 25
        barr1 = vp.box(pos=vp.vector(x10,0,0),
                        length= xL, height=0.75, width=0.01, color = vp.color.red)
        barr2 = vp.box(pos=vp.vector(0,0,0),
                        length=self.L, height=0.75, width=0.01, color = vp.color.red)
        barr1 = vp.box(pos=vp.vector(x20,0,0),
                        length=xL, height=0.75, width=0.01, color = vp.color.red)
    def single_stilt(self, dl):
        self.dl = dl
        sep = self.dl/2
        L = 50
        x0 = 50/2 + sep
        barr1 = vp.box(pos=vp.vector(x0,0,0),
                        length= L, height=0.75, width=0.01, color = vp.color.red)
        barr2 = vp.box(pos=vp.vector(-x0,0,0),
                        length= L, height=0.75, width=0.01, color = vp.color.red)

def diffract(lbd, dl, n, L = 20, rate = 75):
    vp.rate = rate
    fd = Stilt()
    if n == 1:
        fd.single_stilt(dl)
    if n == 2:
        fd.double_stilt(L, dl)
    plain = Wave(0, 0)
    plain.plain(lbd)
    fact = dl/lbd
    if fact == 1:
        ang = pi
        y0 = 0
    elif fact > 1:
        ang = -0.79*fact + 2.36
        h = sqrt(abs(1-(dl/2))**2)
        y0 = -h
    elif fact< 1:
        ang = 3.93*fact - 0.79
        y0 = 0
    else:
        ang = 0
    if n == 1:
        sing = Wave(0, 0)
        rad = dl/2
        while rad < 50:
            sing.wave(rad, ang)
            rad += lbd
    if n == 2:
        rad = dl/2
        x = (L/2)+(dl/2)
        doub1 = Wave(x, y0)
        doub2 = Wave(-x, y0)
        while rad < 50:
            doub1.wave(rad, ang)
            doub2.wave(rad, ang)
            rad += lbd


diffract(0.8, 0.6, 2, L=5)
