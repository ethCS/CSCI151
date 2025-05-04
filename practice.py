import stdio
import stdarray
import sys

a = [0,1,2,2,1,0,3,1,2]
m=4

def rescale(a:list):
    least = min(a)
    most = max(a)
    difference = most - least

    for i in range(len(a)):
        a[i] = (a[i] - least) / difference

    return a


def histogram(a:list, m:int):
    new_array = stdarray.create1D(m, 0)
    return_str = ""
    
    for num in a:
            new_array[num] += 1
    return new_array

print(str((histogram(a, m))))
print(str(rescale(a)))