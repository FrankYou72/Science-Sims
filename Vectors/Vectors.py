from turtle import *
from math import sin, cos, tan, radians, degrees, atan,acos, asin, sqrt

def axis():
    xaxis = Turtle()
    xaxis.speed(0)
    xaxis.goto(-600, 0)
    xaxis.goto(600, 0)
    yaxis = Turtle()
    yaxis.setheading(90)
    yaxis.speed(0)
    yaxis.goto(0, -300)
    yaxis.goto(0, 300)


wn = Screen()

menu = textinput('MENU', "O que você deseja fazer?\n[1] - Decomposição de vetores\n[2]Soma de vetores.")


def decomp():
    length = 10*float(textinput('Módulo', 'Insira o módulo do vetor'))
    angle = radians(float(textinput('Ângulo', 'Insira o ângulo que o vetor faz com o eixo x')))

    vector_X = length*cos(angle)
    vector_Y = length*sin(angle)

    axis()

    vector = Turtle()
    vector.pensize(2)
    vector.color('blue')
    vector.setheading(degrees(angle))
    vector.forward(length)
    vector.write(f'({round(vector_X, 2)}, {round(vector_Y, 2)})')

    vx = Turtle()
    vx.color('green')
    vx.fd(vector_X)

    vy = Turtle()
    vy.color('red')
    vy.setheading(90)
    vy.fd(vector_Y)

class VecModAng():
    def __init__(self, mod, ang):
        self.mod = mod
        self.ang = ang
        self.comp_x = self.mod*cos(radians(self.ang))
        self.comp_y = self.mod*sin(radians(self.ang))
        self.comps = (self.comp_x, self.comp_y)
    def draw(self, color):
        v = Turtle()
        v.color(color)
        v.shapesize(1)
        v.setheading(self.ang)
        v.pensize(2)
        v.fd(self.mod)
        v.write(f'({round(self.comp_x, 2)}, {round(self.comp_y, 2)})')
    def dot(self, vecB):
        return self.comp_x*vecB.comp_x + self.comp_y*vecB.comp_y

class VecXY():
    def __init__ (self, i, j):
       self.i = i
       self.j = j
       self.mod = sqrt(self.i**2 + self.j**2)
       if self.i < 0:
           self.ang = degrees(atan(self.j/self.i)) + 180
       else:
            self.ang = degrees(atan(self.j/self.i))
    
    def draw(self, color):
        v = Turtle()
        v.color = color
        v.shapesize(1)
        v.setheading(self.ang)
        v.pensize(2)
        v.fd(self.mod)
        v.write(f'({round(self.i, 2)}, {round(self.j, 2)})')

    def dot(self, vecB):
        return self.i*vecB.i + self.j*vecB.j



def somaV():
    axis()
    modo = textinput('Modo', 'Os vetores estão em termos de\n[1]módulo/ângulo ou\n[2]componentes?')
    if int(modo) == 1:
        mod1 = 15*float(textinput('Módulo do vetor 1', 'Insira o módulo'))
        ang1 = float(textinput('Ângulo do vetor 1', 'Insira o ângulo'))
        mod2 = 15*float(textinput('Módulo do vetor 2', 'Insira o módulo'))
        ang2 = float(textinput('Ângulo do vetor 2', 'Insira o ângulo'))
        vec1 = VecModAng(mod1, ang1)
        vec1.draw('blue')
        vec2 = VecModAng(mod2, ang2)
        vec2.draw('red')
        print(f'Vetor 1: ({vec1.comp_x}, {vec1.comp_y})')
        print(f'Vetor 2: ({vec2.comp_x}, {vec2.comp_y})')
        R_x = vec1.comp_x + vec2.comp_x
        print(f'Resultante X: {vec1.comp_x} + {vec2.comp_x} = {R_x}')
        R_y = vec1.comp_y + vec2.comp_y
        print(f'Resultante Y: {vec1.comp_y} + {vec2.comp_y} = {R_y}')
        mod_R = sqrt(R_x**2 + R_y**2)
        if R_x < 0:
            ang_R = degrees(atan(R_y/R_x)) + 180
        else:
            ang_R = degrees(atan(R_y/R_x))
        print("angulo :" , ang_R, ' graus')
        vecR = VecModAng(mod_R, (ang_R))
        vecR.draw('green')
    elif int(modo) == 2:
        i1 = 15*float(textinput('î, vetor 1', 'Componente Horizontal'))
        j1 = 15*float(textinput('^j, vetor 1', 'Componente Vertical'))
        i2 = 15*float(textinput('î, vetor 2', 'Componente Horizontal'))
        j2 = 15*float(textinput('^j, vetor 2', 'Componente Vertical'))
        vec1 = VecXY(i1, j1)
        vec1.draw('blue')
        vec2 = VecXY(i2, j2)
        vec2.draw('red')
        i_R = vec1.i + vec2.i
        print(f'Resultante X: {vec1.i} + {vec2.i} = {i_R}')
        j_R = vec1.j + vec2.j
        print(f'Resultante Y: {vec1.j} + {vec2.j} = {j_R}')
        mod_R = sqrt(i_R**2 + j_R**2)
        if j_R == 0:
            if i_R <= 0:
                ang_R = 180
            else:
                ang_R = 0
        elif i_R < 0:
            ang_R = degrees(atan(j_R/i_R)) + 180
        else:
            ang_R = degrees(atan(j_R/i_R))
        print("angulo :" , ang_R, ' graus')
        vecR = VecModAng(mod_R, (ang_R))
        vecR.draw('green')

        


if int(menu) == 1:
    decomp()
elif int(menu) == 2:
    somaV()


wn.mainloop()