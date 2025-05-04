import stdio
import sys
import stddraw

def draw(n,x0, y0, x1, y1, x2, y2):

    x0, y0 = 0.1, 0.1
    x1, y1 = 0.9, 0.1
    x2, y2 = 0.5, 0.9

    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        stddraw.line(x0, y0, x1, y1)
        stddraw.line(x1, y1, x2, y2)
        stddraw.line(x2, y2, x0, y0)
    stddraw.setPenRadius(0.1)
    stddraw.show()

    draw()

        #draw(n-1, n/2)
        # draw(n-1, n/2)
        # draw(n-1, n/2)