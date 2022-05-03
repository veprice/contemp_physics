# Virginia Price
# Program 1: Amazing Axle
# Solution
# Due Jan 15

''' This program simulates a rod rotating about an axle that moves to the right under a force F = <0.1 N, 0, 0>.

The initial position of the rod + axle system is determined by user input through a click + drag system.'''

'''
Answers to written problems go here

'''
from vpython import *

## SET UP USER INTERFACE FUNCTIONS ##
drag = False    # Tells program if it's currently dragging rod+axle
done = True     # Keeps user from moving rod around while sim is still running

# Executed when user pushes down on left mouse button
def down():
    global drag,rod
    # check to see if previous run has finished
    if done == True:
        rod.axis = vec(1,0,0) # reset rod rotation or funny things happen
        drag = True # Turn on mouse dragging
    else:
        print('Please wait until the current run has finished before moving the rod.') # be patient ya nerd

# Executed while user holds down mouse button
def move():
    global drag,axle,rod,done
    if drag==True and done==True:
        # change position of rod + axle
        rod.pos = scene.mouse.pos - vec(1/2,0,0)
        axle.pos = scene.mouse.pos - vec(0,0,.4/2)

# To be executed when user lets go of left mouse button
def up():
    global drag,done
    if drag==True:
        drag = False    # stop dragging the rod+axle
        done = False    # simulation has started
        play_sim()

# Bind mouse actions to their respective functions
scene.bind("mousedown",down)
scene.bind("mousemove",move)
scene.bind("mouseup",up)

# This function plays the simulation once the rod + axle are dropped.
def play_sim():
    global rod,axle,gd,I,done # get global variables

    ## RESET BLOCK ##

    # Reset all movement variables to zero
    axle.v = vec(0,0,0)
    rod.L = vec(0,0,0)
    rod.omega = vec(0,0,0)
    rod.theta = 0
    rod.KE = 0

    # Reset plot data
    gd.omega_v_t.data = [[0,0]]
    gd.theta_v_t.data = [[0,0]]

    ## EXECUTE SIMULATION ##
    # Initialize time-based while loop
    dt = 0.0001
    t = 0

    # Execute for 7 seconds
    while t < 7:
        rate(1/dt)
        torque = vec(0,0,3*cos(5*t))

        # Update axle position
        axle.v += axle.F/2*dt
        axle.pos += axle.v*dt
        rod.pos += axle.v*dt

        # Update rod physics
        rod.L += torque*dt      # torque changes L
        rod.omega = rod.L/I     # find new angular velocity
        mag_omega = dot(rod.omega,norm(axle.axis))  # get mag(omega)
        rod.dtheta = mag_omega * dt # theta changes by this much
        rod.theta += rod.dtheta     # add dtheta to total rotation

        rod.KE = I*mag_omega**2/2   # get kinetic energy

        # Insert code to angle & rod position here
        rod.rotate(angle=rod.dtheta, axis=axle.axis, origin=axle.pos)

        # Add points to plots
        gd.omega_v_t.plot(t,mag_omega)
        gd.theta_v_t.plot(t,rod.theta)

        t = t + dt

    print('The final angle of the rod is: ' + '{:0.5}'.format(rod.theta) + ' radians')
    print('The final angular speed is: ' + '{:0.5}'.format(mag_omega) + ' radians per second')

    done = True

    return


### SET UP ###
# This code runs on startup, placing the rod and cylinder and
# Physical Constants
M = 2
Lrod = 1
R = 0.1
Laxle = 4*R
I = (1/12)*M*Lrod**2 + (1/4)*M*R**2


# Set up rotating rod
rod = cylinder(pos=vec(-1,0,0), radius=R, color=color.orange,
               axis=vec(Lrod,0,0))
rod.L = vec(0,0,0)      # Angular momentum of rod
rod.omega = vec(0,0,0)  # Angular frequency w(omega)
rod.theta = 0           # Initial angular position
rod.dtheta = 0          # Initial dtheta
rod.KE = 0              # Initial kinetic energy

# Set up axle
axle = cylinder(pos=vec(-1+Lrod/2,0,-Laxle/2), radius = R/6,
                color=color.red, axis=vec(0,0,4*R))
axle.F = vec(0.1,0,0)   # Force on axle
axle.v = vec(0,0,0)     # Initial velocity of axle

# Set up graphing area
gd = graph(title='<b>Angular Properties</b>',
      xtitle='Time (<i>t</i>)', ytitle='',
      foreground=color.black, background=color.white)

# Set up data lines
gd.omega_v_t = gcurve(color=color.red, label='Angular velocity')
gd.theta_v_t = gcurve(color = color.blue, label='Theta')
