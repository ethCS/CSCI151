###############################
#Ethan Elliott
#im3.py
#Assignment 11a (Part 3/3)
#Example usage: "python im3.py mandrill.jpg"
#Creates 3 photos in one, one of each from left to right: red, green, blue component(s).
###############################

#modules i needed for proper functionality
import sys
import stddraw
import luminance
from color import Color
from picture import Picture

#since gray would default all of the y's to the same num, i figured defaulting the colors i don't want to 0 would get me the color i desire.
#so in these 3, i only get the one i need. R,G,B in that order. The rest are 0's. This ensures that i get the correct color for use later.
def toRed(pixel):
    red = luminance.luminance(pixel)
    return Color(int(round(red)),0,0)

#same rules apply to this one as well.
def toGreen(pixel):
    green= luminance.luminance(pixel)
    return Color(0,int(round(green)),0)

#and the final one...
def toBlue(pixel):
    blue = luminance.luminance(pixel)
    return Color(0,0,int(round(blue)))

#for these i decided to make a function for getting each color instead of doing one function for all of them.
#calling "toRed() uses the luminance module in order to return the correct values
def red_component(photo):
    #create object of red
    photo_red = Picture(photo.width(), photo.height())
    for col in range(photo.width()):
        for row in range(photo.height()):
            pixel = photo.get(col, row)
            red_val = toRed(pixel)
            photo_red.set(col, row, red_val)
    return photo_red

#same thing, i just copied/pasted from red_component, this one just does green instead.
def green_component(photo):
    #create object of green
    photo_green = Picture(photo.width(), photo.height())
    for col in range(photo.width()):
        for row in range(photo.height()):
            pixel = photo.get(col, row)
            green_val = toGreen(pixel)
            photo_green.set(col, row, green_val)
    return photo_green

#and lastly, the blue one...
def blue_component(photo):
    #create object of blue
    photo_blue = Picture(photo.width(), photo.height())
    for col in range(photo.width()):
        for row in range(photo.height()):
            pixel = photo.get(col, row)
            blue_val = toBlue(pixel)
            photo_blue.set(col, row, blue_val)
    return photo_blue

def main():
    #filename from user
    picture_filename = str(sys.argv[1])
    #create object from constructor picture.py
    photo = Picture(picture_filename)
    #since the assingment wanted 3 images in one, the width would be multiplied by num of images, so in that case, that's gonna be three. 
    #height of course stays the same since we aren't changing the height.
    stddraw.setCanvasSize((photo.width() * 3), photo.height())
    #setting the default scale to what i mentioned earlier with it being multiplied by 3 due to 3 images being shown.
    stddraw.setXscale(0, photo.width() * 3)
    #height not changing, once again...
    stddraw.setYscale(0, photo.height())

#This was the hardest part. I originally had these as float values, but realized that it wouldn't work with any image if i used that method.
#instead, with this method, it always get the center, then offsets in opposing directions for red and blue, respectively. Since green is in the
#middle, it doesn't need to be offset in any way. It's already in the center. So that's unchanged. I tested this with many images, it's universal now!!!!
    stddraw.picture(red_component(photo), ((photo.width() * 3) / 2) - photo.width(), photo.height() / 2)
    stddraw.picture(green_component(photo), (photo.width() * 3) / 2, photo.height() / 2)
    stddraw.picture(blue_component(photo), ((photo.width() * 3) / 2) + photo.width(), photo.height() / 2)

#show to user
    stddraw.show()

#test client
if __name__ == "__main__":
    main()