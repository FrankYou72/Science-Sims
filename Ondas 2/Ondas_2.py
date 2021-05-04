import vpython as vp
import math

x = -20
spheres = []

for b in range(20):
    part = vp.sphere(pos = vp.vector(x, 0, 0))
    spheres.append(part)
    x += 2

t = 0
dt = 0.05

while t < 200:
    vp.rate(20)
    phi = 0
    w = math.pi/2
    for s in spheres:
        s.pos.y = 4*vp.sin(w*t + phi)
        phi += 0.4
    t += dt
