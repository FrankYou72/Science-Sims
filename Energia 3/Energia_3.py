from vpython import *
import numpy as np
tela = canvas(title='Energy 3', width=1200, height=600, center=vector(0,-5,0))

arco = shapes.arc(radius = 10, angle1 = np.pi , angle2 = 2*np.pi)
rampa = extrusion(pos = vec(0, -5, 0), shape = arco, path = [vec(0, 0, -5), vec(0, 0, 5)])

corpo = sphere(pos = vec(-9, 0, 0), color = color.red, massa = 1, vel = vector(0,0,0),
               peso = vec(0, -1, 0), normal = vec(0, 0, 0))

#
#Initial values
#
m = corpo.massa; g = -10; P = m*g; R = 9
t = 0; dt = 1E-3
L = 0; w = 0; I = m*R**2 ; ang = acos(corpo.pos.x/R)
atr = 0 ; atr_torque = 0

def coeficiente(n):
    return n

mu = slider(bind = coeficiente, value = 0)
scene.append_to_caption('\n\n')
#
#Vectors
#
Peso = arrow(pos = corpo.pos, axis = vec(0, -1, 0), length = 5,
             shaftwidth = 0.2, color = color.green)
Normal = arrow(pos = corpo.pos, axis = vector(0,0,0),
               color = color.yellow,
               shaftwidth = 0.2)
Res = arrow(pos = corpo.pos, axis = vec(0,0,0),
               color = vec(0.5, 1, 1), length = 5,
               shaftwidth = 0.2)
Atrito = arrow(pos = vector(-10, 0, 0), axis = vector(0, 0, 0),
               color = vec(1, 0, 0), length = 5,
               shaftwidth = 0.2)
#
#Energy bars
#
Epot = cylinder(pos = vector(-5, 6, 0), axis = vector(1, 0, 0), length = 9,
                color = color.green, emissive = True)
Ecin = cylinder(pos = vector(-5, 3, 0), axis = vector(1, 0, 0), length = 9,
                color = color.red, emissive = True)
#
#Text displays
#
EpText = label(pos = Epot.pos, xoffset = -40, text = '')
EcText = label(pos = Ecin.pos, xoffset = -40, text = '')
EmText = label(pos = vector(7.5, 5, 0), text = '', color = color.yellow)
AltText = label(pos = vector(-15, 4, 0), text = '', color = color.green)
vText = label(pos = vector(0, 0, 0), text = '', color = vec(0.5, 0.75, 1))
muText = label(pos = vector(-15, -9, 0), text = '', color = color.red)
gv = gcurve(color = color.red)
#
#Iteration code
#
while t < 400:
    # set rate of frame
    #
    rate(400)
    #
    #set parameters
    #
    Peso.pos = corpo.pos
    Peso.length = 5
    x = corpo.pos.x
    y = corpo.pos.y
    i = -cos(ang)/abs(cos(ang))
    j = -1
    h = y + 9
    m = corpo.massa
    #
    #calculate Torque, angular acceleration
    #
    Tau = P*R*-cos(ang) - atr_torque # -+-- = -  for left, + for the right
    alpha = Tau/I
    #
    #Calculate net acceleration and net force
    a = alpha*R # - for left, + for the right
    FR = m*a # - for left, + for the right
    #
    #Decompose net force
    #
    FRx = (FR*-sin(ang)*-cos(ang))*i #left => POS ; right => NEG
    FRy = (FR*cos(ang))*j # ALWAYS NEG
    #send parameters to arrow object Res
    #
    Res.axis = vector(FRx/abs(FR), FRy/abs(FR), 0) #LEFT (,,)
    Res.length = abs(FR/P)*5
    Res.pos = corpo.pos
    # Solve for Normal
    #
    Nx = FRx #left => POS ; right => NEG OK
    Ny = FRy - P
    N = sqrt(Nx**2 + Ny**2)
    Normal.axis = vector(Nx/abs(N), Ny/abs(N), 0)
    Normal.pos = corpo.pos
    Normal.length = abs(N/P)*5
    #
    #Kinematics
    #
    w += alpha*dt
    v = w*R*dt
    vx = -v*sin(ang)
    vy = -v*cos(ang)
    x += vx
    y += vy
    vel = sqrt(vx**2 + vy**2)
    if y < -9.0:
        y = -9.0
    
    corpo.pos = vector(x, y, 0)
    ang += w*dt

    #
    Ep = m*-g*h/R
    Epot.axis.x = Ep
    Ec = 0.5*(m/R)*(w*R)**2
    Ecin.axis.x = Ec
    EpText.text ='U = ' + str(round(Ep, 2)) + ' J'
    EcText.text = 'K = ' + str(round(Ec, 2)) + ' J'
    EmText.text = 'U + K = ' + str(round(Ec + Ep, 2)) + ' J'
    AltText.text = 'h = ' + str(round(h, 2)) + ' m'
    vText.text = 'v = ' + str(round(abs(w*R), 2)) + ' m/s'
    muText.text = 'mu = ' + str(round(mu.value, 2))
    #gv.plot(atr, t)
    #
    #Set up friction
    #
    atr = N*mu.value*(-abs(vx)/vx)
    atr_torque = atr*R
    Atrito.axis = vector(atr*sin(ang)*-i,
                         atr*abs(cos(ang)),
                         0)
    Atrito.length = abs(atr/P)*5
    Atrito.pos = vector(9.5*cos(ang), 9.5*-sin(ang), 0)
    t += dt
    
#Código finalizado por Franklin Santos às 11:31 de 05/10/2020