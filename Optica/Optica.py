import turtle
import math
import random

wn = turtle.Screen()

axispos = turtle.Turtle()
axisneg = turtle.Turtle()
mirrorup = turtle.Turtle()
mirrordown = turtle.Turtle()

axispos.goto(400, 0)
axisneg.goto(-400, 0)
axisneg.left(180)

mirrorup.goto(0, 150)
mirrorup.left(90)
mirrordown.goto(0, -150)
mirrordown.rt(90)

focus = turtle.Turtle()
focus.shape('circle')
focus.penup()
focus.shapesize(0.5, 0.5)
focus.speed(0)

Title = turtle.Turtle()
Title.hideturtle()
Title.penup()
Title.goto(-100, 200)
Title.pendown()

f = -(turtle.numinput('DISTÂNCIA FOCAL', ' ', default = random.randint(-200, 200) ,
                      minval = -200, maxval =200))

p = -(turtle.numinput('POSIÇÃO DO OBJETO', ' ', default = random.randint(1, 300) ,
                      minval = 1, maxval =300 ))

o = turtle.numinput('ALTURA DO OBJETO', ' ', default = 75 ,minval = 1, maxval = 75 )

if p == f:
    Title.write('Espelho CÔNCAVO\n IMAGEM IMPRÓPRIA',
                    font = ('Arial', 16, 'normal'))
    pl = 10000
    i = 1000
    focus.goto(f, 0)
    focus.write('f', font = ('Arial', 16, 'normal'))

    obj = turtle.Turtle()
    obj.penup()
    obj.goto(p, 0)
    obj.pendown()
    obj.lt(90)
    obj.goto(p, o)
    obj.write('OBJETO')
    lr = turtle.Turtle()
    lr.hideturtle()
    lr.penup()
    lr.goto(p, o)
    lr.pendown()
    lr.pencolor('yellow')

    lr2 = lr.clone()

    lr.goto(0, o)
    lr.goto(f, 0)
    lr.goto(pl, i)
    lr2.goto(f, 0)
    lr2.goto(0, i)
    lr2.goto(pl, i)

else:
    pl = (1/f - 1/p)**(-1)

    A = -pl/p
    
    i = A*o

    focus.goto(f, 0)
    focus.write('f', font = ('Arial', 16, 'normal'))

    obj = turtle.Turtle()
    obj.penup()
    obj.goto(p, 0)
    obj.pendown()
    obj.lt(90)
    obj.goto(p, o)
    obj.write('OBJETO')

    lr = turtle.Turtle()
    lr.hideturtle()
    lr.penup()
    lr.goto(p, o)
    lr.pendown()
    lr.pencolor('yellow')

    lr2 = lr.clone()

    lr.goto(0, o)
    lr.goto(f, 0)
    lr.goto(pl, i)

    if f > 0:
        Title.write('Espelho CONVEXO', font = ('Arial', 16, 'normal'))
        lr2.goto(0,i)
        lr2.goto(pl, i)
    elif abs(f) > abs(p) and f < 0 :
        Title.write('Espelho CÔNCAVO', font = ('Arial', 16, 'normal'))
        lr2.goto(0, 0)
        lr2.goto(pl, i)
    else:
        Title.write('Espelho CÔNCAVO', font = ('Arial', 16, 'normal'))
        lr2.goto(f, 0)
        lr2.goto(0, i)
        lr2.goto(pl, i)


    im = turtle.Turtle()
    im.penup()
    im.goto(pl, 0)
    if i < 0:
        im.setheading(-90)
    else:
        im.seth(90)
    im.pendown()
    im.goto(pl, i)
    im.write('IMAGEM')

    print('DISTÂNCIA FOCAL: ', -f)
    print('POSIÇÃO DO OBJETO: ', -p)
    print('ALTURA DO OBJETO: ', o)
    print('POSIÇÃO DA IMAGEM: ', '%.2f' % -pl)
    print('ALTURA DA IMAGEM: ', '%.2f' % i)
    print('AUMENTO: ', '%.2f' % A)




wn.mainloop()
