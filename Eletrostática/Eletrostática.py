import turtle as tt
from math import sqrt

wn = tt.Screen()


class Carga:
    def __init__(self, carga, massa, raio, cor):
        self.carga = carga
        self.massa = massa
        self.raio = raio
        self.cor = cor
        self.velx = 0
        self.vely = 0
        self.vel = sqrt((self.velx)**2 + (self.vely)**2)
        self.T = tt.Turtle()
        self.T.shape('circle')
        self.T.shapesize(raio, raio)
        self.T.penup()
        self.T.color(cor)
        self.x = 0
        self.y = 0
    def move(self, x, y):
        self.x = x
        self.y = y
        self.T.goto(x, y)
        self.T.pendown()
    def dist(self, t):
        d = sqrt((self.x - t.x)**2 + (self.y - t.y)**2)
        return d
box = tt.Turtle()

box.penup()
box.goto(-150, 150)
box.pendown()
for i in range(4):
    box.fd(300)
    box.rt(90)
box.hideturtle()


Q1 = Carga(-7, 0.2, 1, 'blue')
Q2 = Carga(6, 0.4, 1, 'red')
Q1.velx = 0.2
Q1.vely = -0.3
Q2.vely = 0.3
Q2.velx = -0.2

Q1.move(-149,100)

Q2.move(149, -100)

t = 0
dt = 0.007
k = 90
x1 = Q1.x
x2 = Q2.x
y1 = Q1.y
y2 = Q2.y


while t < 300:
    d = (Q1.dist(Q2))
    if abs(d) < 20:
        Fel == 0
        Q1.velx *= -1
        Q2.velx *= -1
        Q1.vely *= -1
        Q2.vely *= -1
        q = Q1.carga + Q2.carga
        Q1.carga, Q2.carga = q, q
    else:
        Fel = k*(Q1.carga * Q2.carga)/d**2
    a1 = -Fel/Q1.massa
    a2 = Fel/Q2.massa
    dx = (Q1.x - Q2.x)
    dy = (Q1.y - Q2.y)
    a1x = -dx*a1/d
    a1y = -dy*a1/d
    a2x = -dx*a2/d
    a2y = -dy*a2/d
    Q1.velx += a1x*dt
    Q1.vely += a1y*dt
    Q2.velx += a2x*dt
    Q2.vely += a2y*dt
    if abs(Q1.x) > 150:
        Q1.velx *= -1
    if abs(Q1.y) > 150:
        Q1.vely *= -1
    if abs(Q2.x) > 150:
        Q2.velx *= -1
    if abs(Q2.y) > 150:
        Q2.vely *= -1
    x1 += Q1.velx
    y1 += Q1.vely
    x2 += Q2.velx
    y2 += Q2.vely
    Q1.move(x1, y1)
    Q2.move(x2, y2)

    t += dt


wn.mainloop()
