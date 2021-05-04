from vpython import *
from math import sqrt, cos, sin, atan, pi

tela = canvas(width = 1000, height = 700)

ls = 40
cs = 40
c0 = 400
vecs = []

R = 1
G = 0
B = 0

C1 = sphere(pos = vector(0,55,0), radius = 10, color = vec(R, G, B))
C2 = sphere(pos = vector(0,-55, 0), radius = 10, color = vec(0, G, 1))

M = 300

for l in range(ls):
    l0 = -390
    for c in range(cs):
        u1 = M*(c0-C1.pos.x)/((c0-C1.pos.x)**2 + (l0-C1.pos.y)**2)
        u2 = M*(c0-C2.pos.x)/((c0-C2.pos.x)**2 + (l0-C2.pos.y)**2)
        u = u1 - u2
        v1 = M*(l0-C1.pos.y)/((c0-C1.pos.x)**2 + (l0-C1.pos.y)**2)
        v2 = M*(l0-C2.pos.y)/((c0-C2.pos.x)**2 + (l0-C2.pos.y)**2)
        v = v1 - v2
        vet = sphere(pos = vector(c0, l0, 0), color = color.white, radius = 0.5,
                     axis = vector(u, v, 0))
        vecs.append(vet)
        l0 += 20
    c0 -= 20

arrows = []
for v in vecs:
    a = attach_arrow(v, 'axis', shaftwidth = 2, color = vec(1, 1, 0))
    arrows.append(a)
        
for t in arrows:
    t.color = vec(0.5, 0.6, 0.7)