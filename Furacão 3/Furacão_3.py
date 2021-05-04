#Attempt to simulate the spiral/circular movement of particles in a fluid.
#In this case I tried to model a hurricane/tornado

from vpython import *
import random
import math
import numpy

# Set up scene
tela = canvas(height = 650, width = 1340, background = vec(0,0,0.2),
              center = vector(0, 0, 0))

#Create the platform: 1 square base with 5 concentrical circles

#'chao' is the ground. It will barely appear since it's of the same color as the background
#however it will be seen of light reflection
chao = box(pos = vector(0, -15, 0), height = 0.1, width = 80, length = 80, color = vec(0,0,0.2))
level1 = extrusion(path=[vec(0, -14.9, 0), vec(0, -14.8, 0)], shape = shapes.circle(radius = 30),
                   pos = vec(0, -14.9, 0), color = vec(0.6, 0, 0))
level2 = extrusion(path=[vec(0, -14.8, 0), vec(0, -14.7, 0)], shape = shapes.circle(radius = 24),
                   pos = vec(0, -14.8, 0), color = vec(0.6, 0.6, 0))
level3 = extrusion(path=[vec(0, -14.7, 0), vec(0, -14.6, 0)], shape = shapes.circle(radius = 18),
                   pos = vec(0, -14.7, 0), color = vec(0, 0.6, 0))
level4 = extrusion(path=[vec(0, -14.6, 0), vec(0, -14.5, 0)], shape = shapes.circle(radius = 12),
                   pos = vec(0, -14.6, 0), color = vec(0, 0.6, 0.6))
level5 = extrusion(path=[vec(0, -14.5, 0), vec(0, -14.6, 0)], shape = shapes.circle(radius = 6),
                   pos = vec(0, -14.5, 0), color = vec(0, 0, 0.6))

#Creating the air particles (in this sim, I consider bunches of mass as particles)
Parts = [] #Particle list
Poss = [] #Particle positions list

#loop to create particles in semi-random positions:
for r in range(224):
    x = random.randint(-30, 30)
    #For the height (y) I use numpy.choice to spread the particles not uniformly, but dependant of the height
    y = numpy.random.choice([-5, -4, -3 ,0, 4, 8, 14, 21, 29, 35],
                            p=[0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.09, 0.08, 0.07, 0.06])
    z = random.randint(-30, 30)
    d = sqrt(x**2 + z**2)
    if d == 0:
        d = 0.1 #Avoiding zero division error
    #In order to make easier the iteration I set up initial velocity as the velocity of a uniform circular movement
    vx = -z/d
    vz = x/d
    # If the velocity is too low the particle doesn't go round, but oscilates in a almost straigth line so we set a limit
    #In reality the particle speeds are too high and there's always collisions to change it.
    lim = 0.3
    if abs(vx) <= lim:
        vx = 0.5
    if abs(vz) <= lim:
        vz = 0.5
    #Actually creating the particle
    p = sphere(pos = vector(x, y, z), radius = 0.5,  vel = vector(vx, 0, vz), make_trail = True,
               trail_radius = 0.05, retain = 15)
    Parts.append(p) #Putting particle in particle list
    Poss.append(p.pos) #Putting position in position list

tela.waitfor('click') # Mechanism to control the flow of the program

#legenda is the subtitle to explain the presentation, it's in pt-br
legenda = label(pos= vec(-90, 25, 0), text='''Evaporação de água:
>>>Redução da pressão embaixo
>>>Aumento da pressão em cima''',
          xoffset=0, yoffset=0, height=24, box = False, color = vec(1, 0.5, 0.5), align = 'left')


#Now I make all the particles in a radius of 32 go up and leave an empty space in the middle
tela.waitfor('click')
legenda.visible = False 
for _ in range(60):
    rate(20)
    for p in Parts:
        x = round(p.pos.x, 2)
        z = round(p.pos.z, 2)
        d = sqrt(x**2 + z**2)
        if d <= 32:
            p.make_trail = False
            i = Parts.index(p)
            Poss.pop(i)
            y = round(p.pos.y, 2)
            vy = 0.7
            h = abs(y-15)
            if h >= 30:
                vy = 0.1
            y += vy
            p.vel.y = vy
            p.pos.y = y
            Poss.insert(i,p.pos)

#now they can stop going up
for p in Parts:
    p.vel.y = 0
    p.make_trail = True

tela.waitfor('click')

#Text presentation

legenda.text = '''Baixa pressão na região central:
>>>Efeito "ralo"'''
legenda.visible = True
centro = cylinder(pos = vec(0, -14.5, 0), axis = vec(0, 60, 0), radius = 20, opacity = 0.25,
                  color = color.red)
tela.waitfor('click')

centro.visible = False
p2 = sphere(pos = vector(15, 10, 0), radius = 0.5,  vel = vector(vx, 0, vz), make_trail = True,
               trail_radius = 0.05, retain = 15)
legenda.text = '''A pressão resultante em cada ponto
é o resultado da pressão de todas as direções.'''
tela.waitfor('click')

legenda.text = '''A pressão sempre será menor perto do
"ralo" e maior longe dele, causando uma
pressão resultante na direção central'''
legenda.visible = False
tela.center = p2.pos
pf = arrow(pos = vec(19, 10, 0), axis = vec(-4, 0, 0), color = color.red)
pfl = label(pos = pf.pos, text = 'Pressão de fora', xoffset = 10, yoffset = 20)
tela.waitfor('click')
pd = arrow(pos = vec(13, 10, 0), axis = vec(2, 0, 0), color = color.yellow)
pdl = label(pos = pd.pos, text = 'Pressão de dentro', xoffset = -10, yoffset = -20)
tela.waitfor('click')
pd.visible, pdl.visible, pf.visible, pfl.visible = False, False, False, False
pr = arrow(pos = p2.pos, axis = vec(-4, 0, 0), color = color.red)
prl = label(pos = pr.pos, text = 'Pressão resultante', xoffset = 10, yoffset = 20)
tela.waitfor('click')

legenda.pos = p2.pos
legenda.text = '''Pressão  é diretamente proporcional
à força. Assim a pressão gerará
uma força centrípeta'''
legenda.visible = True
tela.waitfor('click')
pr.axis = vec(-6, 0, 0)
prl.text = 'Força resultante'
tela.waitfor('click')

prl.visible = False
tela.center = vec(0,0,0)
legenda.text = '''A força centrípeta causa o movimento
circular/espiral característico dos
tornados e furacões'''
tela.waitfor('click')

#Sim's standard parameters

t = 0 #time
dt = 0.01 #time increment
#P0 = 1E5 #Pressure at the eye of the hurricane. Normal pressure at sea level = 1E5.
         #Set it between 1E4 and 1E5. Best results between 9.2E4 and 9.8E4.
         #This is basically the core of the sim. The difference between the pressure set
         #and 1E5 will dictate the behavior of the hurricane. The less you set the pressure
         #more violent will be the spinning winds.
massa = 1E-9 #mass of the 'particle'
area = 4E-12 #area of the 'particle' in wich the force will cause pressure

#Labels

bar = label(pos=vec(0, 30, 0), text='', space=30, height=24, border=4, font='sans') #pressure at the eye
spd = label(pos = vec(35, 15, 0), text = '', space=30, height=24, border=4, font='sans') #windspeed at the periphery
spd0 = label(pos=vec(0, 30, 0), text='', xoffset = -40, yoffset = 25, space=30, height=24,
             border=4, font='sans') #windspeed near the eye

t = 0 #time
dt = 0.01 #time increment
massa = 1E-9 #mass of the 'particle'
area = 4E-12 #area of the 'particle' in wich the force will cause pressure

def IPres(P):
    return P

sl = slider(bind = IPres, min = 9E4, max = 1E5, value = 9.8E4)

tela.append_to_caption('\n\n')


while t < 400:
    P0 = sl.value
    rate(20) #rate of frames
    for p in Parts:
        i = Parts.index(p) #get the index of each particle
        Poss.pop(i) #takes its position out of the list
        #round up the position vaues to make the math easiear less messy
        x = round(p.pos.x, 2)
        z = round(p.pos.z, 2)
        y = round(p.pos.y, 2)
        #assign variables for velocities
        vx = p.vel.x
        vz = p.vel.z
        vy = p.vel.y
        d = sqrt(x**2 + z**2)
        h = abs(y-15) #height
        if h == 0: #preventing unexpected results
            h = 1
        dP = ((1E5-P0)/42)*(d**2)*(1/h) #This is the most important equation of this program.
                                        #It returns the difference of pressure between internal and external part
                                        #of a particle in a point, in relation to the hurricane eye.
        F = dP*area #From dp, calculate force
        a = F/massa #From force, calculate acceleration
        if d < 0.03: #If particle get to the center, d = 0 and the program will crash,
                     #so if it gets too close we randomly put it to go round a little bit more and farther
            ax = -a*x*d
            az = -a*z*d
            vx += ax*dt
            vy -= 0.004*dt
            vz += az*dt
            x = random.choice([-2, 2])
            z = random.choice([-2, 2])
        else: #for the rest, we apply circular motion concepts.
              #The vertical velocity will increase also due to gravity
            ax = -a*x/d
            az = -a*z/d
            vx += ax*dt
            vy -= 0.004*dt
            vz += az*dt
            x += vx
            z += vz
        v = round(sqrt(vx**2 + vz**2), 2) #get the composite velocity
        if v > 2*sqrt(d*a): #correct if velocity is too high in order to not losing the particle
            vx *= 0.9
            vz *= 0.9
        if v < (sqrt(d*a)): #correct if velocity is too low in order to the particles not to fall in the eye.
            vx = -2*z/d
            vz = 2*x/d
        y += vy
        #reassign values
        p.vel.x = vx
        p.vel.z = vz
        p.vel.y = vy
        p.pos.x = x
        #check if particle get to the ground
        if y < -15:
            p.vel.y = 1
            p.pos.y = y
        else:
            p.pos.y = y
        p.pos.z = z
        #check for collisions
        for posi in Poss:
            if p.pos.x <= posi.x + 0.4 and p.pos.x >= posi.x - 0.4:
                if p.pos.y <= posi.y + 0.4 and p.pos.y >= posi.y - 0.4:
                        if p.pos.z <= posi.z + 0.4 and p.pos.z >= posi.z - 0.4:
                            p.vel.x *= -0.9
                            p.vel.y *= -0.9
                            p.vel.z *= -0.9

        #Get the data after a loop
        Pp = ((1E5-P0)/42)*(42**2) 
        Fp = Pp*area
        ap = Fp/massa
        F0 = P0*area
        a0 = F0/(massa*4)

        Poss.insert(i,p.pos)
        windspd = round(sqrt(ap*30), 0)
        windspd0 = round(sqrt(a0), 0)
    t += dt
    bar.text = str(P0/100) + ' mbar'
    spd.text = str(windspd*2) + ' km/h'
    spd0.text = str(windspd0*2) + ' km/h'

