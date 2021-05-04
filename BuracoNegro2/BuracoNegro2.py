import turtle
from math import pi, sqrt, ceil, floor

wn = turtle.Screen()
wn.bgcolor('black')
wn.colormode(255)
wn.screensize(950, 650)
wn.setup(width = 1.0, height = 1.0, startx = None, starty = None)

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
vxs = [-24, -30, -15.5]
vys = [-15, -3, -26]
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

input('Pressione Enter para iniciar')
#Draw the black hole's accretion disk
    
while t< 100:
    dt = 0.125
    xd = disk.xcor()
    yd = disk.ycor()
    red = red + 1.12*dt
    green = green + 2.54*dt
    blue = blue + 1.38*dt
    rd = disk.distance(bh.xcor(), bh.ycor())
    vd = sqrt(vdy**2 + vdx**2)
    ad = (vd**2)/rd
    adx = -ad*xd/rd
    ady = -ad*yd/rd
    vdx += adx*dt
    vdy += ady*dt
    xd = xd + vdx*dt
    yd = yd + vdy*dt
    disk.color(arred(red), arred(green), arred(blue))
    disk.goto(xd, yd)
    t += dt

input('Pressione a tecla ENTER pra continuar')

#Arrows

arrow = turtle.Turtle()
arrow.color('green')
arrow.penup()
arrow.goto(400, 250)
arrow.hideturtle()
arrow.showturtle()
arrow.pendown()
arrow.setheading(240)
arrow.goto(pla.xcor(), pla.ycor())
input('Pressione Enter')
arrow.hideturtle()
arrow.clear()
arrow.penup()



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
        if foton.distance(pla.xcor(), pla.ycor()) <= 20:
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

wn.mainloop()