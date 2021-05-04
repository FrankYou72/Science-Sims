import turtle
from math import pi, sqrt, ceil, floor

wn = turtle.Screen()
wn.bgcolor('black')
wn.colormode(255)

#Set up BH

bh = turtle.Turtle()
bh.shape('circle')
bh.shapesize(4, 4)

#Set up photons

fot = turtle.Turtle()
fot.penup()
fot.speed(0)
fot.goto(400, 250)
fot.left(180)
fot.color('yellow')
fot.hideturtle()
fot2 = fot.clone()
fot3 = fot.clone()

fot.pendown()
fot2.pendown()
fot3.pendown()

fotons = [fot, fot2, fot3]

#set up accretion disk

red = 140
green = 1
blue = 1
disk = turtle.Turtle()
disk.penup()
disk.speed(3)
disk.goto(45, 0)
disk.color(red, green, blue)
disk.hideturtle()
disk.pendown()
disk.pensize(3)

#set up stars

star1 = turtle.Turtle()
star1.shape('circle')
star1.penup()
star1.speed(0)
star1.goto(400, 250)
star1.color('yellow')

'''star2 = star1.clone()
star3 = star1.clone()

star2.goto(400, 100)
star3.goto(400, 150)'''

#set up planet

pla = turtle.Turtle()
pla.shape('circle')
pla.penup()
pla.speed(0)
pla.goto(-300, -200)
pla.color('blue')


#Set up initial values

G = 0.1
mbh = 1000000
mfot = 0.1
t = 0
dt = 0.075
vxs = [-24, -30, -15]
vys = [-15, -3, -24]
vdx = 0
vdy = 15

#set rounding function

def arred(a):
    from math import floor, ceil
    if type(a) == float:
        if a - floor(a) < 0.5:
            return int(floor(a))
        else:
            return int(ceil(a))
    elif type(a) == int:
        return a

#Draw the black hole's accretion disk
    
while t< 100:
    dt = 0.125
    xd = disk.xcor()
    yd = disk.ycor()
    red = red + 1.12*dt
    green = green + 2.59*dt
    blue = blue + 1.43*dt
    rd = disk.distance(bh.xcor(), bh.ycor())
    vd = sqrt(vdy**2 + vdx**2)
    ad = (vd**2)/rd
    adx = -ad*xd/rd
    ady = -ad*yd/rd
    vdx += adx*dt
    vdy += ady*dt
    xd = xd + vdx*dt
    yd = yd + vdy*dt
    disk.color(arred(red), int(round(green))-1, arred(blue))
    disk.goto(xd, yd)
    t += dt

input('Pressione a tecla ENTER pra continuar')

#Release the photons

for foton in fotons:
    dt = 0.04
    t = 0
    while (t < 50):
        x = foton.xcor()
        y = foton.ycor()
        r = foton.distance(bh.xcor(), bh.ycor())
        ind = fotons.index(foton)
        vx = vxs[ind]
        vy = vys[ind]
        if r <= 35:
            foton.hideturtle()
            foton.clear()
            t = 50
        if foton.distance(pla.xcor(), pla.ycor()) <= 30:
            t = 50
        if r > 20:
            Fg = G*mfot*mbh/r**2
            a = Fg/mfot
            ax = -a*x/r
            ay = -a*y/r
            vx = vx + ax*dt
            vxs[ind] = vx
            vy = vy + ay*dt
            vys[ind] = vy
            x = x + vx*dt
            y = y + vy*dt
            foton.goto(x, y)
        t += dt
    input('press enter to continue.')
    
'''
t = 0
dt = 0.05
vxs = [0, 0, 0, 0, 0, 0]
vys = [-30, -30, -30, -30, -30, -30]

fot7 = fot.clone()
fot8 = fot.clone()
fot9 = fot.clone()
fot10 = fot.clone()
fot11 = fot.clone()
fot12 = fot.clone()

fot7.penup()
fot8.penup()
fot9.penup()
fot10.penup()
fot11.penup()
fot12.penup()



fot7.goto(-150, 200)
fot8.goto(-90, 200)
fot9.goto(-20, 200)
fot10.goto(40, 200)
fot11.goto(110, 200)
fot12.goto(160, 200)


fot7.pendown()
fot8.pendown()
fot9.pendown()
fot10.pendown()
fot11.pendown()
fot12.pendown()




fotons2 = [fot7, fot8, fot9, fot10, fot11, fot12,]

while (t < 90):
    for foton in fotons2:
        x = foton.xcor()
        y = foton.ycor()
        r = foton.distance(bh.xcor(), bh.ycor())
        ind = fotons2.index(foton)
        vx = vxs[ind]
        vy = vys[ind]
        if r <= 20:
            foton.clear()
            foton.hideturtle()
            foton.reset()
            fotons2.pop(ind)
            vxs.pop(ind)
            vys.pop(ind)
        elif r >27 and r < 40:
            d = foton.distance(bh.xcor(), bh.ycor())
            a = (30**2)/d
            ax = -a*x/d
            ay = -a*y/d
            vx = -30*y/d
            vxs[ind] = vx
            vy = 30*x/d
            vys[ind] = vy
            x = x + vx*dt
            y = y + vy*dt
            foton.goto(x, y)
        if r >= 36:
            Fg = G*mfot*mbh/r**2
            a = Fg/mfot
            ax = -a*x/r
            ay = -a*y/r
            vx = vx + ax*dt
            vxs[ind] = vx
            vy = vy + ay*dt
            vys[ind] = vy
            x = x + vx*dt
            y = y + vy*dt
            foton.goto(x, y)
        t += dt

t = 0
dt = 0.05
vxs = [30, 30, 30, 30, 30, 30]
vys = [0, 0, 0, 0, 0, 0]

fot13 = fot.clone()
fot14 = fot.clone()
fot15 = fot.clone()
fot16 = fot.clone()
fot17 = fot.clone()
fot18 = fot.clone()

fot13.penup()
fot14.penup()
fot15.penup()
fot16.penup()
fot17.penup()
fot18.penup()



fot13.goto(-400, 80)
fot14.goto(-400, 20)
fot15.goto(-400, -40)
fot16.goto(-400, -100)
fot17.goto(-400, -140)
fot18.goto(-400, -180)

fot13.pendown()
fot14.pendown()
fot15.pendown()
fot16.pendown()
fot17.pendown()
fot18.pendown()




fotons3 = [fot13, fot14, fot15, fot16, fot17, fot18,]

while (t < 90):
    for foton in fotons3:
        x = foton.xcor()
        y = foton.ycor()
        r = foton.distance(bh.xcor(), bh.ycor())
        ind = fotons3.index(foton)
        vx = vxs[ind]
        vy = vys[ind]
        if r == 0:
            r = 1
        if r <= 25:
            foton.clear()
            foton.hideturtle()
            foton.reset()
            fotons3.pop(ind)
            vxs.pop(ind)
            vys.pop(ind)
        elif r > 30 and r < 36:
            d = foton.distance(bh.xcor(), bh.ycor())
            a = (30**2)/d
            ax = -a*x/d
            ay = -a*y/d
            vx = -30*y/d
            vxs[ind] = vx
            vy = 30*x/r
            vys[ind] = vy
            x = x + vx*dt
            y = y + vy*dt
            foton.goto(x, y)
        if r >= 36:
            Fg = G*mfot*mbh/r**2
            a = Fg/mfot
            ax = -a*x/r
            ay = -a*y/r
            vx = vx + ax*dt
            vxs[ind] = vx
            vy = vy + ay*dt
            vys[ind] = vy
            x = x + vx*dt
            y = y + vy*dt
            foton.goto(x, y)
        t += dt

t = 0
dt = 0.05
vxs = [0, 0, 0, 0, 0, 0]
vys = [30, 30, 30, 30, 30, 30]

fot19 = fot.clone()
fot20 = fot.clone()
fot21 = fot.clone()
fot22 = fot.clone()
fot23 = fot.clone()
fot24 = fot.clone()

fot19.penup()
fot20.penup()
fot21.penup()
fot22.penup()
fot23.penup()
fot24.penup()



fot19.goto(-120, -200)
fot20.goto(-50, -200)
fot21.goto(-190, -200)
fot22.goto(20, -200)
fot23.goto(90, -200)
fot24.goto(160, -200)

fot19.pendown()
fot20.pendown()
fot21.pendown()
fot22.pendown()
fot23.pendown()
fot24.pendown()


fotons4 = [fot19, fot20, fot21, fot22, fot23, fot24,]

while (t < 90):
    for foton in fotons4:
        x = foton.xcor()
        y = foton.ycor()
        r = foton.distance(bh.xcor(), bh.ycor())
        ind = fotons4.index(foton)
        vx = vxs[ind]
        vy = vys[ind]
        if r == 0:
            r = 1
        if r <= 25:
            foton.clear()
            foton.hideturtle()
            foton.reset()
            fotons4.pop(ind)
            vxs.pop(ind)
            vys.pop(ind)
        elif r > 30 and r < 36:
            d = foton.distance(bh.xcor(), bh.ycor())
            a = (30**2)/d
            ax = -a*x/d
            ay = -a*y/d
            vx = -30*y/d
            vxs[ind] = vx
            vy = 30*x/r
            vys[ind] = vy
            x = x + vx*dt
            y = y + vy*dt
            foton.goto(x, y)
        if r >= 36:
            Fg = G*mfot*mbh/r**2
            a = Fg/mfot
            ax = -a*x/r
            ay = -a*y/r
            vx = vx + ax*dt
            vxs[ind] = vx
            vy = vy + ay*dt
            vys[ind] = vy
            x = x + vx*dt
            y = y + vy*dt
            foton.goto(x, y)
        t += dt'''

wn.mainloop()

