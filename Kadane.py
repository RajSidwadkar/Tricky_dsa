#Problem is to find the maximum sum of a contiguous subarray within a one-dimensional array of numbers.

from math import inf
numbers = [3, -2, 5, -1, 4, -3, 2, 2, -5, 4]


def Kadane(numbers):
    
    #if all numbers are negative
    if all(n < 0 for n in numbers):
        return max(numbers)

    current_sum = 0
    max_sum = float(-inf)

    for n in numbers:


        current_sum += n

        if current_sum > max_sum:
            max_sum = current_sum

        if current_sum< 0:
            current_sum = 0

    return max_sum


