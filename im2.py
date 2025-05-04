###############################
#Ethan Elliott
#im2.py
#Assignment 11a (Part 2/3)
#Example Usage: "python im2.py mandrill.jpg"
#Purpose: #draws the image horizontally flipped
###############################

#setting the modules I'll need to import
import sys
import stddraw
from picture import Picture

def flip_horizontal(photo):
#predefining vars
    width = photo.width()
    height = photo.height()
#create object from constructor
    flipped = Picture(width, height)
#access each pixel
    for col in range(width):
        for row in range(height):
            pixel = photo.get(col, row)
            #offset the height so it rotates
            flipped.set(height - 1 - row, col, pixel)
        #return for later use
    return flipped


def main():
    #image file name from user stored in cmdline argument i casted to string to prevent errors
    picture_filename = str(sys.argv[1])
    #object creation once again
    photo = Picture(picture_filename)

#func call
    flipped_photo = flip_horizontal(photo)

#setting the defaaults
    stddraw.setCanvasSize(flipped_photo.width(), flipped_photo.height())
#setting picture
    stddraw.picture(flipped_photo)
#show user
    stddraw.show()

#test client
if __name__ == "__main__":
    main()

