# An apple company is having trouble keeping track of how many apples they’re growing and how many apples they are selling,
# and want to know their total profit for each month. Each week, once a week, they get a total count from their harvesters
# on how many apples were harvested for that week. They also get data on how many apples they sell each day, with Thursday
# being the day they sell apples for half off.

# You tell them you can write a function that takes m months apples harvested as an array, where the array contains 4
# entrees for the total apples harvested a month, and n total apples sold each day for a given 30 day month as an array
# (30 entrees in the array, one for each day). If they normally sell apples for $2.50, and it takes $.30 for them to
# harvest an apple. Determine their monthly profits given that the Thursday of each week is a half off day. you can
# assume they sell no apples on saturday and sunday as they are closed.

# m = 4 entrees, each entry is for the total num of apples harvested each week
# n = array - containing apples sold each day of m

#default the array to 30
import stdio
import stdarray
import sys


m = [2000, 1500, 1000, 4000]
n = [0,0,200,250,50,500,100,0,0,50,50,100,300,300,0,0,100,100,150,250,200,0,0,400,400,200,1000,100,0,0]


def monthlyProfits(m:list,n:list) -> int:
    """
    This function takes in 2 arguments, which enter a formula to determine the profit margins for a fruit company.

    m = (array) 4 entrees, each element being the total num of apples harvested for that week.
    n = (array) containing apples SOLD each day in m

    returns: How profitable as an int, dollars, per month.
    """

    cost_to_sell_apple = 2.50
    cost_to_harvest_apple = 0.30
    thursday_cost = cost_to_sell_apple / 2

    new_values = []
    new_values_total_profit = 0
    monthlyApplesHarvestCost = 0
    thursday = False
    dayCounter = 5

    for i in range(len(n)):
        if n[i] == 0:
            continue
        if i % dayCounter == 0:
            thursday = True
        if thursday == True:
            dayCounter += 7
        if thursday == True:
            new_profit = (n[i] * thursday_cost)
            new_values.append(new_profit)
            thursday = False
            continue
        new_profit = (n[i] * cost_to_sell_apple)
        new_values.append(new_profit)

    for i in new_values:
        new_values_total_profit += i

    for i in range(len(m)):
        monthlyApplesHarvestCost += m[i] * cost_to_harvest_apple
    return new_values_total_profit - monthlyApplesHarvestCost

stdio.writeln("$" + str(monthlyProfits(m,n)))