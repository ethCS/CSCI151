####################################
#Ethan Elliott
#2-12-25
#dice.py
#assignment 4
#comment was made at the bottom of the code
#purpose of this code is to simulate the rolling of two dice and calculating the probability of the sum of the dice
####################################

import sys
import stdio
import random
import stdarray
#I imported these modules for the following reasons:
#sys is for cmdline arguments, stdio is for input/output, random is for random number generation, stdarray is for creating arrays

n = int(sys.argv[1])
#input from user via cmdline argument # of trials

my_probabilities = stdarray.create1D(13, 0.0)
#creating an array with 13 elements all starting off at float 0.0

#this loop below runs for n times which calculates the sum and increments the array
for i in range(n):
    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    total = dice_one + dice_two
    my_probabilities[total] += 1.0
for j in range(2, 13):
    my_probabilities[j] /= n
    #dividing the total by n to get the probability, just like how shown in the textbook example we did

#below is from the textbook. but to explain, it's a nested for loop- for finding the float probabilities
probabilities = stdarray.create1D(13, 0.0)
for i in range(1, 7):
    for j in range(1, 7):
        probabilities[i+j] += 1.0
for k in range(2, 13):
    probabilities[k] /= 36.0

#printing out the results on each iteration. i used an f string because it's easier for me. 2 to 13 because that's the range of the dice.
#casted to a string so it would print out correctly...
stdio.writef('Exact results\n')
for i in range(2, 13):
    stdio.writef('Probability the sum of die is ' + str(i) + ": " + str(probabilities[i]) + '\n')

#this one uses the my_probabilities array that i created instead of the one from the textbook
stdio.writef('\nEmpirical results\n')
for i in range(2, 13):
    stdio.writef('Results the sum of die is ' + str(i) + ": " + str(my_probabilities[i]) + '\n')

#same as before.. except i'm subtracting to find the difference
stdio.writef('\nDifference\n')
for i in range(2, 13):
    prob = (round(probabilities[i] - my_probabilities[i], 3))
    stdio.writef('Difference when the sum is ' + str(i) + ": " + str(prob) + '\n')

# I was able to get them to match at lowest: 800k trials.
# But the higher I go, the more it tends to match.
# However, even at 2 million, i wasn't able to get it to work on every single trial.
# At 2.5mill, i was able to match the empirical results to the exact results 11 times in a row.