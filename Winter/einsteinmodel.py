from vpython import *
from random import *


# Create buttons
def Al_click():
   global Al
   add_E(Al)
   print('Aluminum currently has ' + str(Al.E) +' energy quanta.')

def Pb_click():
   global Pb
   add_E(Pb)
   print('Lead currently has ' + str(Pb.E) +' energy quanta.')

button(bind=Al_click,text='+1 Energy to Al')
button(bind=Pb_click,text='+1 Energy to Pb')

# This function adds 1 quantum of energy to the x,y,or z of the given atom
def add_E(atom):
   i = randint(1,3)
   if i == 1:
      atom.E.x += 1
   elif i == 2:
      atom.E.y += 1
   elif i == 3:
      atom.E.z += 1

# Set up walls
wall_dims = vec(.025,2,2)
Al_box = []
wall1 = box(pos=vec(-2,0,0),axis=vec(1,0,0), size=wall_dims,opacity=0.2)
for i in range(6):
   Al_box.append(box(pos=vec(

# Set up the system
Al = sphere(pos=vec(-1,0,0),radius=0.1,color=vec(.7,.7,.7))
Al.E = vec(0,0,0)

Pb = sphere(pos=vec(1,0,0),radius=0.17,color=vec(.5,.5,.7))
Pb.E = vec(0,0,0)

Al_springs = []


