"""
Program a function sumAverage(arr) where arr is an array containing arrays full of numbers, for example:

sum_average([[1, 2, 2, 1], [2, 2, 2, 1]])
First, determine the average of each array. Then, return the sum of all the averages.

All numbers will be less than 100 and greater than -100.
arr will contain a maximum of 50 arrays.
After calculating all the averages, add them all together, then round down, as shown in the example below:

"""

from math import floor

arr = [[1, 2, 2, 1], [2, 2, 2, 1]]
def sum_average(arr):
    arr_average = 0
    for item in arr:
        arr_average += sum(item)/len(item)
    return floor(arr_average)


"""
Shortest solutions :

def sum_average(r):
  return floor(sum(sum(rr)/len(rr) for rr in r))
  
  
sum_average = lambda a:floor(sum([sum(x)/len(x) for x in a]))

"""