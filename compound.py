############################################
# ethan elliott
# compound.py
# continuously compounded interest, 1.2.21
# csci151
# 1-27-25
############################################

# -------PURPOSE -------
# the purpose of this program is to calculate and write the amt of money you would
# have if you invested it at a given interest rate compounded continuously.

# ------- HOW TO USE -------
# Enter the following to run this file, and substitute values accordingly: "python compound.py YEARS, PRINCIPLE, ANNUAL INTEREST RATE"

# ------- CODE EXPLANATION -------
# these modules below are required in order to execute the program.
import sys
# sys is necessary for cmd line argument
import math
# math is necessary for euler num in the formula
import stdio
# necessary for duce's preferred method of printing text


years = float(sys.argv[1])
# storing the first argument in the years variable
principal = float(sys.argv[2])
# storing the second argument in the principle variable
annual_interest_rate = float(sys.argv[3])
# storing the last argument in the annual_interest_rate variable

formula = principal * math.e**(annual_interest_rate * years)
# this formula is where I am plugging in all of the user generated variables for computation
rounded_formula = round(formula, 2)
# using round functionality w/ argument of .2 decimal places in order to shorten float value length

stdio.writeln(rounded_formula)
# printing results to the user with a newline
