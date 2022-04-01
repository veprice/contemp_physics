"""
Recitation 3 Solution
Author: Virginia Price
Purpose: Short simulation of the Earth and Jupiter orbiting around the Sun!

Also on glowscript.org:
https://glowscript.org/#/user/virginia.e.price/folder/contempphys/program/03orbit
"""

#import necessary libraries
from vpython import *

#Define all constants
AU = 1.5e11     # Distance between Earth and Sun (m)
G = 6.67e-11    # Gravitaitonal Constant (m^3/kg*s^2)
Msun = 2e30     # Mass of the Sun (kg)
Mearth = 6e24   # Mass of the Earth (kg)
rearth = 1*AU   # Distance from sun to Earth (m)
Mjupiter = 2e27     # Mass of Jupiter (kg)
rjupiter = 5.5*AU   # Distance from sun to Jupiter (m)
yr = 3.15e7     # Length of a year (s)

# Define the window scale
scene.range = 6*AU
scene.autoscale = 0
lamp = local_light(pos=vec(0,0,0))

#Let there be light
sun = sphere(pos = vec(0,0,0),
             radius=0.25*AU,
             color=color.yellow,
             texture="https://i.imgur.com/sWARNps.jpg")
sun.m = Msun
sun.v = vector(0,0,0)
s_orbit = curve(color=color.yellow)

# On the second day Virginia created the Earth
earth = sphere(pos=vec(rearth,0,0),
               radius=0.075*AU,
               texture=textures.earth)
earth.m = Mearth
earth.v = vector(0,30000,0)         # velocity of Earth in m/s
e_orbit = curve(color=color.blue)   # earth's orbit

#Time to make this system a bit more regal
jupiter = sphere(pos=vec(rjupiter,0,0),
                 radius=0.2*AU,
                 texture = "https://i.imgur.com/5FbL240.jpg")
jupiter.m = Mjupiter
jupiter.v = vector(0,13000,0)
j_orbit = curve(color=color.red)    #Jupiter's orbit


# Set time parameters
dt = 0.005*yr   # Break a year into 200 steps
t = 0           # Set initial time

# Start the clock!
while (t < 20*yr):
    rate(50)        #I upped the rate b/c 20 was real slow
    earth.pos = earth.pos + dt*earth.v   # r = vt
    e_orbit.append(earth.pos) # update the trail

    jupiter.pos = jupiter.pos + dt*jupiter.v
    j_orbit.append(jupiter.pos)

    sun.pos = sun.pos + dt*sun.v
    s_orbit.append(sun.pos)


    # Calculate gravitational forces!
    # First calculate all the position vectors
    r_SE = sun.pos - earth.pos
    r_SJ = sun.pos - jupiter.pos
    r_EJ = earth.pos - jupiter.pos

    #shove it into F = Gm1m2/r^2*rvec
    F_se = G * sun.m*earth.m * (r_SE) / pow(mag(r_SE),3)
    F_sj = G * sun.m*jupiter.m * (r_SJ) / pow(mag(r_SJ),3)
    F_ej = G * earth.m*jupiter.m * (r_EJ) / pow(mag(r_EJ),3)

    # Update the velocities of all bodies
    earth.v = earth.v + F_se/earth.m  * dt - F_ej/earth.m*dt
    jupiter.v = jupiter.v + F_sj/jupiter.m * dt + F_ej/jupiter.m*dt
    sun.v = sun.v + -F_se/sun.m * dt + -F_sj/sun.m*dt

    t = t+dt    #take a time step
