"""
Virginia Price
Recitation Assignment #4
Created 10/11/2018
Last modified 4/1/2022

This code models masses on springs and simple harmonic motion!

Also on glowscript.org:
https://glowscript.org/#/user/virginia.e.price/folder/contempphys/program/04spring
"""

from vpython import *


""" Set some Constants"""
L = 3           # Equilibrium length of soring (m)
yceiling = 1.5  # position of the yceiling (m)
g = vec(0,9.8,0)         #gravity (m/s^2)

y0 = yceiling - L   # Set the equilibrium position of the spring

"""Set the scene"""
ceiling = box(pos = vec(0,yceiling,0),  #Make a box with a granite texture
              length=6,                 #dimensions
              width = 4,
              height = 0.2,
              texture = textures.granite)#make it stone

scene.autoscale = 0

spring = helix(pos=vec(0,yceiling,0),  # make a spring on the ceiling
                axis = vec(0,-L,0),     # make it vertical
                radius = 0.1*L)         # Set the roundness

ball = sphere(pos=vec(0,y0,0),        #put a ball on the spring
                radius = 0.2*L)
ball.v = vec(0,0,0)                   # the ball has 0 initial velocity
ball.eq = vec(0,y0,0)

""" Widget Functions! """
# Spring Constant
def K(k):
    refresh()
    return
scene.append_to_caption('\n')
k = slider(bind=K, min=1, max=50, step=0.1, value=25, length=100)
scene.append_to_caption(' Spring constant (k): ')
k_val = wtext(text=k.value)
scene.append_to_caption(' N/m\n\n')

# Initial Displacement
def DY(dy):
    refresh()
    return

scene.append_to_caption('\n')
dy = slider(bind=DY, min=-L, max=L, step=0.1, value=0, length=100)
scene.append_to_caption(' Initial Displacement: ')
dy_val = wtext(text=dy.value)
scene.append_to_caption(' m\n\n')

# Mass Slider + display
def M(m):
    refresh()
    return

# When sliders update, restart simulation flag
restart = True
def refresh():
    global restart
    restart = True
    return

scene.append_to_caption('\n')
m = slider(bind=M, min=0.1, max=5, step=0.1, value=1, length=100)
scene.append_to_caption(' Ball Mass (m): ')
m_val = wtext(text=m.value)
scene.append_to_caption('kg\n\n')

# Period Display
scene.append_to_caption('Theoretical Period (T): ')
T_th_val = wtext(text='Waiting...')
scene.append_to_caption(' s^-1\n')

scene.append_to_caption('Experimental Period (T): ')
T_exp_val = wtext(text='Waiting...')
scene.append_to_caption(' s^-1\n')

"""Run the simulation"""
dt = 0.01
flag = 0

while True:
    rate(1/dt)

    # Reset simulation if sliders have changed
    if restart == True:
        # Update slider values
        k_val.text = k.value
        m_val.text = m.value
        dy_val.text = dy.value

        # Reset ball + timer
        t = 0
        flag = 0
        ball.pos = vec(0, y0+dy.value,0)
        ball.v = vec(0,0,0)
        ball.F = vec(0,0,0)

        # Calculate Periods
        T_th = 2*pi/sqrt(k.value/m.value)
        T_th_val.text = '{:0.3}'.format(T_th)
        T_exp_val.text = 'Waiting...'
        restart = False

    # First find the total force on the ball
    # Finding this later will result in a compound oscillatory effect
    ball.F = -k.value*(ball.pos - ball.eq) - m.value*g

    # Update the ball's speed & position
    ball.v = ball.v + ball.F/m.value*dt
    ball.pos = ball.pos + ball.v*dt

    #stretch the spring
    spring.axis = ball.eq + ball.pos

    # Start timer to measure period
    if (ball.v.y>0 and flag==0):
        flag = 1
        P_i = t
    # End timer to measure period + calculate
    if (ball.v.y<0 and flag == 1):
        P = (t-P_i)*2
        T_exp_val.text = '{:0.3}'.format(P)
        flag = 2
    # Update time
    t = t+dt
