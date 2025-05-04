#############################
#Ethan Elliott
#race_car.py
#CSCI151
#2-23-25
#Quiz: Race Car & Projectile Motion
#note: i tried doing the physics problem (quiz question #2) initially for a few hours but kept getting errors. did problem #1 instead.
#############################

import stddraw
import random
#necessary modules for drawing and getting rng values

stddraw.setCanvasSize(1280, 720)
#i used 720p's ratio for the background

#setting the horizontal and veritcal init
stddraw.setXscale(0, 1)
stddraw.setYscale(0, 1)

#i was gonna make an actual car with this but can't figure out how to do it... so here's a square.
def car(horizontal, vertical, color):
    stddraw.setPenColor(color)
    stddraw.filledSquare(horizontal, vertical, 0.01)

#i wanted a barrier between both cars, so i put a yellow line
def barrier():
    stddraw.setPenColor(stddraw.YELLOW)
    stddraw.filledRectangle(0, cars_vertical - 0.05, 1, 0.007)

#I used my code from the checkered.py project last week to make this checkered finish line code below:)
def finish_line():
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setPenRadius(0.01)
    stddraw.line(1, 0, 1, 1)

#modulo op checks for even/odd and assigns different colors to each square in my specifidd location. this code was by mrs. duce.
    for i in range(10):
        for j in range(10):
            if ((i+j) % 2 != 0):
                stddraw.setPenColor(stddraw.WHITE)
            else:
                stddraw.setPenColor(stddraw.BLACK)
            stddraw.filledRectangle(1 - 0.01, i * 0.1, 0.02, 0.1)

#setting the vert to half so it's in the middle of the screen
#horizontal starts at the leftmost area of the screen
car1_horizontal = 0
car2_horizontal = 0
cars_vertical = 1/2

#the 100 value is the num of the track length
tracklen = 100
#empty str init
who_won = ""

#iteration through length of track and calling the functions defined above
for i in range(tracklen):
    stddraw.clear(stddraw.BLACK)
    car(car1_horizontal, cars_vertical, stddraw.RED)
    car(car2_horizontal, cars_vertical - 0.1, stddraw.WHITE)
    barrier()
    finish_line()
#speed of race, lower is faster. 35 seems good to me.
    stddraw.show(35)
#i wanted to use random.randrange but that didn't work with floats so google said i needed to use uniform() instead:
    car1_horizontal += random.uniform(0.01, 0.02)
    car2_horizontal += random.uniform(0.01, 0.02)

#if either cars got to the end
    if car1_horizontal >= 1 or car2_horizontal >= 1:
        break

#assigning the empty strting from earlier w/ a name
if car1_horizontal >= 1:
    who_won = "red"
else:
    who_won = "white"

#i prefer black so i made the background black
stddraw.clear(stddraw.BLACK)

#changing text color depending on who won
if who_won == "red":
    stddraw.setPenColor(stddraw.RED)
else:
    stddraw.setPenColor(stddraw.WHITE)

#i think monospace is cool and modern looking so i choose that
stddraw.setFontFamily("monospace")
stddraw.setFontSize(20)
#format string lets me show var's on screen easy, first 2 arguments are location/orientation specific for where it presents itself
stddraw.text(1/2, 1/2, f"the winner is the {who_won} car.")
#show to user
stddraw.show()