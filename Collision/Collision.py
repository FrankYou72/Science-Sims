import turtle
import math
import random


wn = turtle.Screen()

#Create area

parede = turtle.Turtle()
parede.penup()
parede.goto(-180, -160)
parede.pendown()
parede.speed(0)
for _ in range(2):
    parede.fd(360)
    parede.lt(90)
    parede.fd(320)
    parede.lt(90)
parede.hideturtle()

#Create balls

class Bola:
    def __init__(self, nome, massa, velx, vely):
        self.nome = nome
        self.massa = massa
        self.velx = velx
        self.vely = vely
        self.posx = random.randint(-180, 180)
        self.posy = random.randint(-160, 160)
    def makeball(self, cor):
        self.nome = turtle.Turtle()
        self.nome.shape('circle')
        self.nome.color(cor)
        self.nome.penup()
        self.nome.goto(self.posx, self.posy)
    def move(self):
        self.nome.goto(self.posx, self.posy)
    def distance(self, x, y):
        return self.nome.distance(x, y)

b1 = Bola('b1', 1, 20, 12)
b1.makeball('red')

b2 = Bola('b2', 2, 13, 21)
b2.makeball('blue')



t = 0
dt = 0.05

Bolas = [b1, b2]

while t < 400:
    for b in Bolas:
        if b.posx <= -175  or b.posx >= 175:
            b.velx = -b.velx
        elif b.posy <= -155 or b.posy >= 155:
            b.vely = -b.vely
        elif b1.distance(b2.posx, b2.posy) < 10:
            b1.velx = -b1.velx
            b2.velx = -b2.velx
            b1.vely = -b1.vely
            b2.vely = -b2.vely
        
        dx = b.velx * dt
        dy = b.vely * dt
        x = b.posx + dx
        y = b.posy + dy
        b.posx, b.posy = x, y
        b.move()


    t += dt
    





wn.mainloop()