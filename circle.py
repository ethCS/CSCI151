###########################
#Ethan Elliott
#circle.py
#2-27-25
#csci151
#assignment 7
###########################

#i only added necessary modules for what needs to be accomplished
import stddraw
import stdarray
import sys
import math
import random

#n represents: how many points do you want? (integer)
n = int(sys.argv[1])
#p represents: what are the chances they'll connect? (float 0.00 --> 1.00)
p = float(sys.argv[2])

#setting up the default values/evnironment for stddraw
stddraw.setCanvasSize(800, 800)
stddraw.setXscale(-1, 1)
stddraw.setYscale(-1, 1)
stddraw.setPenRadius(0.01)
stddraw.setPenColor(stddraw.BLACK)

#adjusting int here will affect sizing but ruin scale at lower argv[1]'s. formula for radius
radius = 1 / math.sqrt(n)

#step between coords
angle_step = (2 * math.pi) / n

#using the built in module to make an array with presets of n rows and two columns
a = stdarray.create2D(n, 2, 0)

#since the coords need to keep changing to make new shapes, i gotta incriment it using the fomrula for the distance ebtween points
for i in range(n):
    #radian angle
    current_angle = i * angle_step
    new_x = radius * math.cos(current_angle)
    new_y = radius * math.sin(current_angle)
#i couldn't get appending to work with the stdarray argument restrictions so i tried indexing on iteration instead. would be easier with a normal list i think.
    a[i][0] = new_x
    a[i][1] = new_y
#make the point
    stddraw.point(new_x, new_y)

#instructions wanted grey so set pen to specific color and i also wanted to make it thin so it's at least visible
stddraw.setPenColor(stddraw.GRAY)
stddraw.setPenRadius(0.0005)

#nested loop, as duce said, for connecting lines
for i in range(n):
    #adding 1 to iteration so no self-comparison
    for j in range(i + 1, n):
        #using rng val and comparing against argv[2], 0 to 1 so it's a float
        if random.uniform(0.0,1.0) <= p:
            #coords reassigned with index of array
            x1, y1 = a[i][0], a[i][1]
            x2, y2 = a[j][0], a[j][1]
            #draw changes
            stddraw.line(x1, y1, x2, y2)

#show user
stddraw.show()