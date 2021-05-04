import turtle
import math

G = 1
m1 = 20000 #Determine a massa do corpo maior, de preferência entre 2000 a 200000
m2 = 100
t = 0
dt = 0.5
#Determine a velocidade inicial
#O valor vx determina o quanto o vetor estará inclinado horizontalmente
#O valor vy determina o quanto o vetor estará inclinado verticalmente
#No início da simulação o planeta está sobre o eixo x, portanto, vy não pode ser 0
#Sugestão: mantenha vy entre 2 e 12
#Sugestão: mantenha vx entre -6 0
vx = -6
vy = 5

wn = turtle.Screen()
wn.bgcolor("Black")


gg = turtle.Turtle()
gg.shape("circle")
gg.shapesize(2)
gg.color("Yellow")
pp = turtle.Turtle()
pp.shape("circle")
pp.speed(0)
pp.penup()
pp.setpos(200, 0)
pp.speed(3)
pp.color("gray")
pp.pendown()

acc = turtle.Turtle()
acc.color("White")
acc.speed(0)
acc.penup()
acc.hideturtle()
vel = turtle.Turtle()
vel.color("red")
vel.speed(0)
vel.penup()
vel.hideturtle()

while (t < 1000):
    
    x = pp.xcor()
    y = pp.ycor()
    t = t + dt
    r = pp.distance(gg.xcor(), gg.ycor())
    Fg = G * m1 * m2/ r**2
    a = Fg/m2
    ax = -a*x/r
    ay = -a*y/r

    vx = vx + ax*dt
    vy = vy + ay*dt
    x = x + vx*dt
    y = y + vy*dt
    v = math.sqrt(vx**2 + vy**2)

    accx = x +(120*ax)
    accy = y +(120*ay)
    velx = x+(20*vx)
    vely = y +(20* vy)

    angle = math.degrees(math.atan(y/x)) + 180
    acc.setheading(angle)
    acc.showturtle()
    acc.goto(x, y)
    acc.pendown()
    acc.goto(accx, accy)
    acc.clear()
    vel.goto(x, y)
    vel.pendown()
    vel.goto(velx, vely)
    pp.goto(x, y)
    vel.clear()
 
wn.mainloop()
