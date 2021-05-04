from vpython import *

x = 10
y = 0

forca = 0.00005
mag = forca*10000
L = 10

barra = cylinder(pos = vector(0, 0, 0), axis = vector(x, y, 0), radius = 0.5, color = color.green)

força = arrow(pos = vector(x, y, 0), axis = vector(-y*mag, x*mag, 0), color = color.red, shaftwidth = 0.1 )

t = 0
dt = 0.1
w0 = 0
w = forca*L*dt
W = label(pos=barra.pos,text= '{:.2f} rad/s'.format(100*w) , xoffset=20, yoffset=50,
          space=30, height=16, border=4, font='sans')
F = label(pos = força.pos, text = '{:} N'.format(mag), yoffset = 60, xoffest = -20,
          space = 30, height = 32, border = 4)


while t < 600:
    rate(10)
    w += forca*L*dt
    x = 10*cos(w*t)
    y = 10*sin(w*t)
    barra.axis.x = x
    barra.axis.y = y
    força.pos = vector(L*cos(w*t), L*sin(w*t), 0)
    força.axis = vector(-y*mag, x*mag, 0)
    F.visible = False
    F = label(pos = força.pos, text = '{:} N'.format(mag), yoffset = 60, xoffest = -20,
              space = 30, height = 32, border = 4)
    W.visible = False
    W = label(pos=barra.pos,text= '{:.2f} rad/s'.format(100*w) , xoffset=20, yoffset=50,
              space=30, height=16, border=4, font='sans')
    t += dt