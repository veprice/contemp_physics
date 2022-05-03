# Virginia Price
# Classes Tutorial
# 5/27/2020

from vpython import *
#a = 1

class Snowperson():
    def __init__(self, SP_height, SP_pos):

        # Define relative heights
        small_R = 1/6 * SP_height
        med_R = 1/3 * SP_height
        big_R = 1/2 * SP_height


        #Define positions
        self.base_pos = SP_pos

        big_pos = SP_pos + vec(0,big_R,0)
        med_pos = big_pos + vec(0,big_R + med_R,0)
        small_pos = med_pos + vec(0,med_R + small_R,0)

        self.bottom = sphere(pos = big_pos, radius = big_R)
        self.middle = sphere(pos = med_pos, radius = med_R)
        self.head = sphere(pos=small_pos, radius = small_R)

        self.nose = cone(pos=small_pos,radius = small_R/5,axis=vec(0,0, 3*small_R), color =color.orange)


    def shovel(self, new_pos):

        self.base_pos = new_pos

        big_pos = new_pos + vec(0,self.bottom.radius,0)
        med_pos = big_pos + vec(0,self.bottom.radius + self.middle.radius,0)
        small_pos = med_pos + vec(0,self.middle.radius + self.head.radius,0)

        self.bottom.pos = big_pos
        self.middle.pos = med_pos
        self.head.pos = small_pos

        self.bottom.color = color.red


# Make a bunch of snow people!
snowpeeps = []
for i in range(10):
    snowpeeps.append(Snowperson(.1+i/10, vec(i-5, 0, 0) ) )
    #print(snowpeeps[i].base_pos)

#snowpeeps[0].shovel(vec(-6,0,0))
