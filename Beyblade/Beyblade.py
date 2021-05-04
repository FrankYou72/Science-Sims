from vpython import *

tela = canvas(width = 1300, height = 800, background = color.blue,
              center = vector(0, 5, 0))


st = shapes.star(n = 4, radius = 4)
oc = shapes.octagon( length=3)

blade = extrusion(path = [vec(0,9,0), vec(0,10,0)], shape = st, color = color.white)
anel = extrusion(path = [vec(0, 8, 0), vec(0,9,0)], shape = oc,
                 color = vec(0.1, 0.1, 0.2))
base = cone(pos = vector(0, 8, 0), axis = vector(0, -2, 0), color = color.red,
            size = vector(2, 4, 4))

beyblade = compound([blade, anel, base], pos = vector(0,0,0), axis = vec(1, 0, 0),
                    w = vector(0, 0, 0))

alfa = sphere(pos=vector(6,0,0), radius=0.1, visible = False, a = vector(0, 0, 0))

t = 0
w = 8
dt = 0.01

while t < 300:
    gto = 10*dt
    alpha = -80*dt
    alfa.a = vector(0,alpha, 0)
    rate(20)
    if w <= 0:
        w = 0
    else:
        w += alpha*dt
    grt = vector(gto/w,-1,(gto/w))
    #beyblade.axis = vec(1, cos(t/20), 0)
    beyblade.w = vec(0, w, 0)
    beyblade.rotate(w, vec(0 , 1, 0 ))
    beyblade.rotate(gto, grt )
    omega = attach_arrow(beyblade, 'w', shaftwidth = 0.5, color = color.green)
    vang = label(pos=omega.pos, text='Velocidade angular: '+str(round(w, 2))+' rad/s',
                 xoffset=-40, yoffset=50, space=30, height=16, border=4, font='sans')
    acc = attach_arrow(alfa, 'a', shaftwidth = 0.5, color = color.yellow)
    al = label(pos=alfa.pos, text='Aceleração angular: '+str(round(alpha, 2))+' rad/s²',
               xoffset=60, yoffset=150, space=30, height=16, border=4, font='sans')
    t +=dt

    #OMG consegui!!! às 20:54 de 03 de Julho de 2020
