##################################
#Ethan Elliott
#filter.py
#4-16-25
#assignment #11
#csci151
#EXAMPLE USAGE: "python filter.py text2.txt" --> outputs to filter_output.txt or shows condensed version in terminal
##################################

#neccessary import modules
import sys
import stdio
import stdarray
from instream import InStream
from outstream import OutStream

#input from user
filename = str(sys.argv[1])
#setting instream wiht input of file name from argv
instream = InStream(filename)
#defining the list of words as str
top_ten = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "i"]
#hardcoding the txt file for outstream
outstream = OutStream("filter_output.txt")

#creating an empty array of size ten
word_array = stdarray.create1D(10, 0)

#creating func for the iterative approach towards solution
def wordChecker(instream, top_ten):
    #getting each word with built in method
    lines = instream.readAllStrings()

#for all of those words, increment counter in array by 1 if it exists
    for element in lines:
        word = element.strip().lower()

        for i in range(len(top_ten)):
            if word == top_ten[i]:
                word_array[i] += 1
                break

    return word_array

#testing function
def main():
    #func call
    wordChecker(instream, top_ten)
    #showing user in the most accurate way as i possibly could trying to mimic trish's example
    #greater than makes it write a line, and the number is how many spaces 
    outstream.writeln(f"{'COUNT':>20}{'WORD':>10}")
    #easiest way to show output to user
    for word in range(10):
        #utilized the same method for printing formatting 
        outstream.writeln(f"{word_array[word]:>20}{top_ten[word]:>10}")
    #output for terminal so operator knows it worked...
    stdio.writeln(str(f"I outputted the contents of the file to the outstream. Here is the unformatted version: {word_array}"))

#self explanatory
if __name__ == "__main__":
    main()