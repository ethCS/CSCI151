###############################
#Ethan Elliott
#im1.py
#Assignment 11a (Part 1/3)
#Example Usage: "python im1.py mandrill.jpg"
#Purpose: Draws a histogram of the frequency of occurrence-
#of each of the 256 grayscale intensities in an inputted file.
###############################

#required modules, picture.py and luminance.py were modules from class.
#i added grayscale.py to the file directly instead of importing. just so i could read it easier...
#reason being is because i struggle with nested loops and visual learning is my preferred way of learning.
#i also reuse the code in my histogram function anyways.
import sys
import stddraw
import luminance
import stdarray
from picture import Picture

#this is from grayscale.py from class that i unchanged. I named it the grayScaleConverter for simplicity.
def grayScaleConverter(pic):
    for col in range(pic.width()):
        for row in range(pic.height()):
            pixel = pic.get(col, row)
            gray = luminance.toGray(pixel)
            pic.set(col, row, gray)

#main function for if __name__ == __main__ below.
def main():
    #getting photo name as a string from the user in cmdline argument
    picture_filename = str(sys.argv[1])
    #making an object from the Picture class for use later on
    photo = Picture(picture_filename)

    #sending that mutable object to the grayscale function for color stripping - this will make all R, G, B values the same so later i can grab whichever one i want.
    grayScaleConverter(photo)
    #histogram function computation call
    grayArray = histogram(photo)
    #drawing the results for user using stddraw module imported earlier
    draw_my_histogram(grayArray)

    #just defining the w/h for my canvas size using the object's methods in picture.py
    width = photo.width()
    height = photo.height()

    #setting those vals
    stddraw.setCanvasSize(width, height)
    stddraw.picture(photo)
    stddraw.show()

#here is where i make the function for calculating the histogram
def histogram(grayScalePhoto):
    #1 dimensional array with 256 values initialized at zero so i can append later
    grayArray = stdarray.create1D(256, 0)

    #nested for each pixel
    for col in range(grayScalePhoto.width()):
        for row in range(grayScalePhoto.height()):
            pixel = grayScalePhoto.get(col, row)
            #since we passed the initial image into the grayscale func, i can grab whichever color i want here.
            lucence_level = pixel.getBlue()
            # add to array
            grayArray[lucence_level] += 1
    #return the val so i can use it as input in the drawing function below
    return grayArray

#time to draw it out
def draw_my_histogram(grayArray):
    #probably could use predefined sizes for this but i chose the good old 720p sizing for this.
    stddraw.setCanvasSize(1280, 720)
    #from 0 to 256 (rgb) in terms of width
    stddraw.setXscale(0, 256)
    #i was going to use a fixed height of an int(1100) but realized you might want other pics to test so i found a way to make it work with any input from user
    #added int(50) so it doesn't abruptly cut off after finishing the drawing. this is more clean this way.
    stddraw.setYscale(0, max(grayArray) + 50)

    #this is where i'm drawing the bars, i messed with these values a lot and i think this looked
    #the nicest but it's really just dependant on your canvas size at the end of the day.
    for i in range(len(grayArray)):
        stddraw.filledRectangle(i, 1, 0.9, grayArray[i])
    #show result to user
    stddraw.show()

#test client
if __name__ == "__main__":
    main()