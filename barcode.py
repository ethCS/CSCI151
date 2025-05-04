#######################
#Ethan Elliott
#barcode.py
#3/10/25
#Assignment #8a
#2.1.34 in the textbook
#######################
#HOW TO USE: type python barcode.py (ZIPCODE HERE), without parenthesis, into the terminal-
#and it will launch the stddraw visualizer for you...
#######################

#getting the required modules
import stddraw
import sys

#input from user
user_input = sys.argv[1]

#i decided to use a dictionary here because it makes sense to me.
#this is the easiest way to define the preset heights of bars in an accessible way
#these key/value pairs are good because the values align directly with the scale of my canvas using stddraw
map_of_heights = {
    1: [0.5, 0.5, 0.5, 1, 1],
    2: [0.5, 0.5, 1, 0.5, 1],
    3: [0.5, 0.5, 1, 1, 0.5],
    4: [0.5, 1, 0.5, 0.5, 1],
    5: [0.5, 1, 0.5, 1, 0.5],
    6: [0.5, 1, 1, 0.5, 0.5],
    7: [1, 0.5, 0.5, 0.5, 1],
    8: [1, 0.5, 0.5, 1, 0.5],
    9: [1, 0.5, 1, 0.5, 0.5],
    0: [1, 1, 0.5, 0.5, 0.5],
}

#initializing this to 2 because i want it to skip every other empty space to print the bar
iterationCounter = 2

#this checks the len of the input and returns a formula that calculates the canvas size
def scaleChecker(user_input):
    length = len(user_input)
    #this is the x axis length, i multiply by 5 because that's how many attributes that 1 int has
    return ((length * 5) + 7) * 2

#so here i'm making the function that will draw the bars
def draw_bars(bar_array):
    """
    The purpose of this function is to draw half or
    full height bars through the stddraw module upon being called.
    """
#i think i had to use global var here because of an issue with mutable vs. immutable objects, i was confused
#because i was able to use the dictionary just fine but that's a good learning experience
    global iterationCounter

#these are the side's guardrails
    stddraw.filledRectangle(0,0,1,1)
    stddraw.filledRectangle(scaleChecker(user_input) - 2,0,1,1)

#every bar per num in the zip code
    for i in bar_array:
        stddraw.filledRectangle(iterationCounter,0,1,i)
        iterationCounter += 2

#i only used this function becAuse she required that we use it, but this iterates through the zipcode
#to print the draw_bars function with specific arguments that we need
def draw_sequence_of_bars(user_input:int):
    """
    The purpose of this function is to draw the sequence
    of the bars to the user upon being called.
    """
    for i in user_input:
        draw_bars(map_of_heights[int(i)])

#getting the checksum using the formula and returning that value
def compute_checksum(user_input):
    """
    The purpose of this function is to compute the checksum
    by adding all of the values in the zip code, then modulo 10
    """
    result = 0

    for i in user_input:
        result = result + int(i)

    checksum = result % 10
    return checksum

#init stuff
stddraw.setXscale(0, scaleChecker(user_input))
stddraw.setYscale(0, 4)
stddraw.setPenRadius(0.001)
stddraw.setPenColor(stddraw.BLACK)

#func calls and showing to things to user
draw_sequence_of_bars(user_input)
draw_sequence_of_bars([compute_checksum(user_input)])
stddraw.show()