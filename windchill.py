############################################
# ethan elliott
# windchill.py
# wind chill, 1.2.22
# csci151, mrs. duce
# 1-27-25
############################################

# -------PURPOSE -------
# the purpose of this program is to compute wind chill temperature

# ------- HOW TO USE -------
# Enter the following to run this file, and substitute values accordingly without the comma(s): "python windchill.py TEMPERATURE, WIND SPEED(MPH)".

# ------- CODE EXPLANATION -------
# these modules below are required in order to execute the program.
import sys
# sys is needed for taking command line arguments
import stdio
# stdio is for standard output

temperature_in_fahrenheit = float(sys.argv[1])
# argument one is stored in this variable for temperature(F).
wind_speed_in_mph = float(sys.argv[2])
# argument two is stored here for wind speed(MPH).

formula = 35.74 + 0.6215 * temperature_in_fahrenheit + \
    (0.4275 * temperature_in_fahrenheit - 35.75) * wind_speed_in_mph**0.16
# all i did here was substitute the variables where they belong in the formula for calculating wind chill.

# all of the following print statements below needed their float variables to be converted to strings prior to execution.
# all of these print statements below will make a newline, exactly how the example illustrated.
stdio.writeln("Temperature = " + str(temperature_in_fahrenheit))
# this prints the temp inputted by the user in argv[1].
stdio.writeln("Wind speed = " + str(wind_speed_in_mph))
# this prints the temp inputted by the user in argv[2].
stdio.writeln("Wind chill = " + str(formula))
# this prints the formulas final computation to the user
# no rounding on this float because this feature was not requested.
