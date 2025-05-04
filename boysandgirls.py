####################################
#Ethan Elliott
#2-10-25
#boysandgirls.py
#assignment 3
#purpose of this code is to simulate the birth of children and calculate the average numbers of children with arrays
####################################
import sys
import stdio
import stdarray
import random
#importing the necessary modules.
#stdio for input/output, stdarray for creating arrays, random for rng values

simulations = int(sys.argv[1])
#trial amount inputted by user on cmdline

#i decided to make a function that takes the argument of simulations as a parameter.
#this function will calculate the average number of children, the frequency of trials with 2, 3, 4, and 5 or more children.
#it will also print out the results.

def main(simulations):
    total_children = 0
    frequency_counter = stdarray.create1D(4, 0)

    for i in range(simulations):
#initializing the variables to zero
        boys = 0
        girls = 0
        children = 0
#while loop runs if boys/girls is zero.
        while boys == 0 or girls == 0:
            if random.random() < 0.5:
#50/50 chance of gender from rng float
                boys += 1
            else:
                girls += 1
            children += 1
#storing total amount in var for calculating avg later
        total_children += children

#there may be a better way to do this, but i used if/elif statements to increment the frequency counter based on the amount of children.
        if children == 2:
            frequency_counter[0] += 1
        elif children == 3:
            frequency_counter[1] += 1
        elif children == 4:
            frequency_counter[2] += 1
        else:
            frequency_counter[3] += 1

#formula for calculating the average number of children
    average_children = total_children / simulations

#printing out the results. i used an f string because it's easier for me.
    stdio.writeln(f'Avg # children: {int(average_children)}')
    stdio.writeln(f'Trials with 2 children: {frequency_counter[0]}')
    stdio.writeln(f'Trials with 3 children: {frequency_counter[1]}')
    stdio.writeln(f'Trials with 4 children: {frequency_counter[2]}')
    stdio.writeln(f'Trials with 5 or more children: {frequency_counter[3]}')

#calling function i made with the simulations as the argument
main(simulations)