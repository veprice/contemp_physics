'''
Virginia Price
Recitation #5 Solution
Created: 10/19/2018
Last Modified: 4/1/2022

Introduction to Relativity
This program simulates a rocket experiencing the effects of relativity as it travels to Alpha Centauri, the nearest star system to us.

I use units where c = 1 for convenience!

On glowscript.org:
https://glowscript.org/#/user/virginia.e.price/folder/contempphys/program/05relativity
'''

# import libraries
from vpython import *
from math import *

# Define some constants
conv_m = 9.461e15               # no. of m in a light year
year = 60*60*24*365.25          # no. of seconds in a year
c = 1                           # Speed of light (ly/y)
ly = 1                          # light year
dist = 4.3                      # trip distance (ly)
m = 1000                        # rocket mass (kg)
L = 0.5                        # rest length of rocket (ly)
flag = 0                        # Set a flag to change v
F = 9800 / conv_m * year**2     # Rocket Force (kg*ly/year^2)


'''Set the scene'''
# make the Earth
earth = sphere(pos=vec(-dist/2,0,0),
               texture = textures.earth,
               radius = 0.15*ly)
earth.t = 0

# make Alpha Centauri
a_cen = sphere(pos=vec(dist/2,0,0),
               radius = 0.25*ly,
               texture = textures.granite,
               color = vec(1,.8,0),
               emissive=True,
               shininess=0)

# Make a rocket
#rocketbody = cylinder(pos=vec(0,0,0),axis=vec(L,0,0),radius = 0.05) # make it a cylinder for now
#rocketpoint = cone(pos=vec(L,0,0),axis=vec(0.5*L,0,0),radius=0.08)

cockpit = ellipsoid(size = vec(0.5,0.5,0.5)*L,opacity = 0.6, color=color.red)
ringy = ring(axis=vector(1,0,0),radius=0.2*L, thickness=.05*L)
wing1 = pyramid(axis=vec(3,0,0),size=vec(1,0.1,0.5)*L)
wing2 = pyramid(axis=vec(-1,0,0),size = vec(1,0.1,0.5)*L)

#rocket = compound([rocketbody,rocketpoint])
rocket = compound([cockpit,ringy,wing1,wing2],pos=earth.pos)

rocket.m = m            # rocket mass (kg)
rocket.F = vec(F,0,0)   # force on rocket (N)
rocket.p = vec(0,0,0)   # rocket initial position
rocket.v = vec(0,0,0)   # rocket initial velocity
rocket.t = 0            # t' = 0


dt = 0.001   # time step (years)

# loop until the rocket is really close to alpha centauri
# not *at* aCentauri because then v is too small to compute
while (rocket.pos.x < a_cen.pos.x-0.01):
    rate(1/dt)

    rocket.p.x += rocket.F.x*dt   # Update rocket momentum (p = p + dF*dt)
    q = rocket.p.x / rocket.m   # change to q for easier calculation of v

    rocket.v.x = q/sqrt((1+q**2))   # find velocity as a fraction of c
    rocket.pos.x += rocket.v.x*dt   # update rocket position
    gamma = 1/sqrt(1-(rocket.v.x**2/c**2))    # calculate rocket gamma

    # flip the thrusters at the 1/2 way point
    if (rocket.pos.x > 0) and (flag == 0):
        rocket.F.x = -rocket.F.x
        wtext(text='The rocket\'s top speed is ' + '{:0.3}'.format(rocket.v.x) + 'c')
        flag = 1            # set flag to 1 --> no more if statement

    rocket.size.x = L/gamma

    # Add to the time for both the rocket and the earth
    rocket.t += dt/gamma    # time dilation!
    earth.t += dt           # Earth is rest frame

wtext(text="The trip takes " + '{:0.3}'.format(earth.t)+ " years according to Earth.\n")
wtext(text="The trip takes " + '{:0.3}'.format(rocket.t) + " years according to the astronauts.")
