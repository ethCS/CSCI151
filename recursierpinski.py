###############################
#Ethan Elliott
#recursierpinski.py
#4/3/25
#csci151
###############################

import stdio
import sys
import stddraw

def draw(n, x0, y0, x1, y1, x2, y2):
    #here is the base case prior to reduction steps for whether input is 0,
    #which practically means that drawing would stop or isn't gonna be possible anymore
    if (n == 0):
        return 0

    #the initial one
    stddraw.line(x0, y0, x1, y1)
    stddraw.line(x1, y1, x2, y2)
    stddraw.line(x2, y2, x0, y0)

    #in order for this concept to work with using the stddraw.line() functionality, it requires me to give an input
    #of 4 positional coordinates, and in order to achieve the smaller recursive triangles, i would need to add the lines total together
    #and then divide it by two in order to see where the halfway point of the line would actually be. this will allow us to have some insight
    #as to where we will begin the next lines.
    half_x0 = ((x0 + x1) / 2)
    half_y0 = ((y0 + y1) / 2)
    half_x1 = ((x1 + x2) / 2)
    half_y1 = ((y1 + y2) / 2)
    half_x2 = ((x2 + x0) / 2)
    half_y2 = ((y2 + y0) / 2)

    #this one is the left
    draw(n - 1, x0, y0, half_x0, half_y0, half_x2, half_y2)
    #the right side
    draw(n - 1, half_x0, half_y0, x1, y1, half_x1, half_y1)
    #the top part
    draw(n - 1, half_x2, half_y2, half_x1, half_y1, x2, y2)

def main():
    #input from user
    n = int(sys.argv[1])
    #pen size
    stddraw.setPenRadius(0.0006)
    #i messed around and tried to get the right sizing here but it wasn't intuitive for me.
    stddraw.setCanvasSize(1000,1000)
    stddraw.setXscale(0,6)
    stddraw.setYscale(0,6)
    #begin the process with calling the function for the first triangle we want to draw().
    draw(n, 0, 0, 6, 0, 3, 6)
    #so we can see it...
    stddraw.show()

#testing client purposes as duce showed
if __name__ == "__main__":
    main()