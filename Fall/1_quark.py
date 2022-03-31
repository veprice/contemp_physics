# First Recitation Solution
# Makes a neutron with two down quarks and one up quarks

# Import packages
from vpython import *
import numpy.random as random

# Make a neutron "shell" to contain the quarks
neutron = sphere(opacity=0.3)

# Generates random number between -0.5 and 0.5
def q_init():
    return random.random() - 0.5

# make empty list for quarks
quarks=[]
# Add quarks to list
quarks.append( cone( radius = 0.1, axis = vec(0, 0.2, 0), color = color.red, type = 'up',
                     pos = vec( q_init(), q_init(), q_init() ),
                     v   = vec( q_init(), q_init(), q_init() ) ))
quarks.append( cone( radius = 0.1, axis = vec(0,-0.2,0), color = color.green, type = 'down',
                     pos = vec( q_init(), q_init(), q_init() ),
                     v   = vec( q_init(), q_init(), q_init() ) ))
quarks.append( cone( radius = 0.1, axis = vec(0,-0.2,0), color = color.blue, type = 'down',
                     pos = vec( q_init(), q_init(), q_init() ),
                     v   = vec( q_init(), q_init(), q_init() ) ))

# Set up time series
dt = 0.05
tmax = 10
t = 0

# Run simulation for t < tmax
while (t<tmax):
    rate(40)    # set frame rate

    # Run through list of quarks
    for q in quarks:
        q.pos += q.v * dt   # Update quark position
        vout = q.pos.dot( q.v ) / mag( q.pos ) # velocity projection along position vector

        # Bounces the quark off the wall if it is too far away
        if (mag(q.pos) > 1 - q.radius) and (vout > 0):
            # Bounce
            q.v = q.v - ( 2 * vout * q.pos ) / mag(q.pos)

    t += dt
    # add timestep

print( 'Done!' ) # notice that simulation has ended
