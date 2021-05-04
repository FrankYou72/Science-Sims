from vpython import *

tela = canvas(width = 1000, height = 600, background = vector(0.6, 0.6, 0.6))

agua = box(pos = vector(0, -3, 0), length = 6, height = 6, width = 6, color = color.cyan, opacity = 0.5)

corpo = box(pos = vector( 0, 0, 0), length = 3, height = 3, width = 3, color = color.red)

g = -10
rho = 1



def Pressure(y, s):
    global agua
    global g
    global rho
    if y <= s:
        return rho*abs(g*(s-y))
    else:
        return 0

def onde(p):
    return p

s = slider(bind = onde, value = 0, min = -3, max = 4)
tela.append_to_caption('\n\n')

peso = arrow(pos = corpo.pos + vector(1, 0, 0), axis = vector(0, -1, 0), length = 1, color = vector(0, 0.25, 0),
             shaftwidth = 0.3)
empuxo = arrow(pos = vector(0, corpo.pos.y - corpo.height/2, 0), axis = vector(0,1,0),
               length = 1, color = vector(1, 0.25, 0), shaftwidth = 0.3)

Empuxo_Label = label(pos = vector(-5, 2, 1), text = '', color = vector(1, 0.25, 0), height = 20)
Peso_Label = label(pos = vector(-5, 1, 1), text = '', color = vector(0, 0.25, 0), height = 20)
Vol_Label = label(pos = vector(-5, 0, 1), text = '', color = vector(0, 0, 0), height = 20)
m = 27

def Emp_s():
    while True:
        l = corpo.height
        superficie = agua.pos.y + agua.height/2
        corpo.pos.y = s.value
        cima = corpo.pos.y + l/2
        baixo = corpo.pos.y - l/2
        if baixo > superficie:
            volsub = 0
        elif cima > superficie:
            volsub = 100*((l**2)*(superficie-baixo))/(l**3)
        else:
            volsub = 100
        P = m*g
        peso.pos = corpo.pos + vector(0, peso.length + l/2, 0)
        peso.length = abs(P)/90
        pcima = Pressure(cima, superficie)
        pbaixo = Pressure(baixo, superficie)
        E = (pbaixo - pcima)*(l**2)
        empuxo.axis = vector(0,E/90,0)
        empuxo.pos.y = corpo.pos.y - l/2 - empuxo.length 
        Empuxo_Label.text = 'Empuxo: ' + str(round(E, 2)) + ' N'
        Peso_Label.text = 'Peso: ' + str(abs(P)) + ' N'
        Vol_Label.text = 'Volume\nSubmerso: ' + str(round(volsub, 2)) + ' %'

def Emp_c():
    h0 = agua.height
    while True:
        l = corpo.height
        superficie = agua.pos.y + agua.height/2
        corpo.pos.y = s.value
        cima = corpo.pos.y + l/2
        baixo = corpo.pos.y - l/2
        if baixo > superficie:
            volsub = 0
        elif cima > superficie:
            volsub = 100*((l**2)*(superficie-baixo))/(l**3)
        else:
            volsub = 100
        P = m*g
        peso.pos = corpo.pos + vector(0, peso.length + l/2, 0)
        peso.length = abs(P)/90
        pcima = Pressure(cima, superficie)
        pbaixo = Pressure(baixo, superficie)
        E = (pbaixo - pcima)*(l**2)
        empuxo.axis = vector(0,E/90,0)
        empuxo.pos.y = corpo.pos.y - l/2 - empuxo.length
        dl = (volsub/100)*l
        x = agua.length
        h = h0 + dl - ((2*dl*(x-l))/x**2)
        agua.height = h
        Empuxo_Label.text = 'Empuxo: ' + str(round(E, 2)) + ' N'
        Peso_Label.text = 'Peso: ' + str(abs(P)) + ' N'
        Vol_Label.text = 'Volume\nSubmerso: ' + str(round(volsub, 2)) + ' %'

Emp_c()