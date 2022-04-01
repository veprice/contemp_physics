'''
Virginia Price
Recitation #6 Solution
Started: Nov 5, 2018
Updated: 4/1/2022

Creating a three-star system
Units:
distance: AU
mass: solar masses
velocity: earth's velocity
time: yr/2π

@glowscript.org:
https://glowscript.org/#/user/virginia.e.price/folder/contempphys/program/06stars
'''
# import these bad boys
from vpython import *
from math import *

# Define a function that will find the center of mass of the star system
def com(starList):
    mx = vec(0,0,0)
    m = 0

    for i in range(len(starList)):
        mx += starList[i].m*starList[i].pos
        m += starList[i].m

    com = mx/m
    return com

''' Add star 1'''
star1 = sphere(pos=vec(-0.5,0,0),
               color=color.red,
               radius=0.10)
star1.m = 1 # one solar mass
star1.v = vec(0,.7,0) #initial velocity
star1.trail = curve(color = star1.color)

''' Add star 2'''
star2 = sphere(pos=vec(0.5,0,0),
               color=color.blue,
               radius=0.15)
star2.m = 2 # two solar masses
star2.v = vec(0,-.7,0) #initial velocity
star2.trail = curve(color = star2.color)

''' Add star 3'''
star3 = sphere(pos=vec(-10,0,0),
               color=color.yellow,
               radius=0.15)
star3.m = 1 # two solar masses
star3.v = vec(0.5,0,0) #initial velocity
star3.trail = curve(color = star3.color)


starList = [star1,star2,star3] #put the stars into a list
#Find the center of mass

#Set up the time for the for loop
t = 0
tmax = 20
dt = 0.001

# Set up plot
g1 = graph( xmin = 0, xmax = tmax,
            xtitle = 'time (years)',
            ytitle = 'Energy (M<sub>sun</sub>•AU<sup>2</sup>/yr<sup>2</sup>)')
ekin = gcurve(graph = g1, color = color.red, label = 'Kinetic Energy')
epot = gcurve(graph = g1, color = color.blue, label = 'Potential Energy')
etot = gcurve(graph = g1, color = color.green, label = 'Total Energy')

while (t<tmax):
    rate(1/dt)
    # reset energies
    K = 0
    U = 0
    # calculate change in velocity &
    for i in range(len(starList)):
        for j in range(len(starList)):
            if i!=j:
                #find the vector between the two stars
                rij = starList[i].pos - starList[j].pos

                #Find the force between the two stars
                Fij = starList[i].m * starList[j].m * rij/pow(mag(rij),3)

                # update the velocity of star j given the force
                starList[j].v += Fij/starList[j].m*dt
                U += -starList[i].m*starList[j].m/mag(rij)

    # Change the position of all stars + calculate kinetic energy
    for i in range(len(starList)):
        starList[i].pos += starList[i].v*dt
        starList[i].trail.append(starList[i].pos)
        K += 0.5*starList[i].m*pow(mag(starList[i].v),2)
    # Update the center of mass of the system
    COM = com(starList)
    # Update the energy plot
    ekin.plot(pos=(t,K))        #kinetic
    epot.plot(pos=(t,U/2))      #potential
    etot.plot(pos=(t,K+U/2))    #total
    t += dt
