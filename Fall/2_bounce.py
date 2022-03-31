"""
Program #2
Testing by Virginia Price

On glowscript.org at:
https://glowscript.org/#/user/virginia.e.price/folder/contempphys/program/02ball
"""
# import your python libraries
from vpython import *
from math import *

# Dr. G's starter code!
dt=0.01
tmax=10.
t=0.
g=9.8
a=vector(0,-g,0)
v0=8.
theta=pi/3

# Define some variables
L = 10.  #box length
H = 0.2 #box height
R = 0.3 #ball radius

scene.autoscale = 0
scene.center = vector(L/2.,0.4*L,0)
scene.scale = 0.7*L

# Make a box
xaxis=box( pos = vector(L/2.,-H/2.,0),
           length = L, height = H, width = L/3.,
           texture = textures.wood )

# Make a ball
ball = sphere(color=color.red,radius=R,pos=vec(0,R,0))
ball.v = vector(v0*cos(theta),v0*sin(theta),0)
trail=curve(color=color.red)


while (t < tmax) :
    rate(1./dt)

    # Update position + velocity using Euler's Method
    ball.pos = ball.pos + ball.v*dt     #r = v*dt
    ball.v = ball.v + a*dt              # here's some gravity! v = a*dt
    trail.append( ball.pos )            # update the trail
    t=t+dt

    # Bounce the ball off the table
    if ((ball.pos.y < ball.radius) & (ball.v.y < 0) & (ball.pos.x<L)):
        ball.v.y = -ball.v.y

        bounce_pos = '{:0.5}'.format(ball.pos.x)
        print('ball bounce at x = '+ bounce_pos + ' m' )
