def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min, max = None, None

    for number in ints:
        if min == None or min > number:
            min = number

        if max == None or max < number:
            max = number

    return (min, max)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail") #random list
print ("Pass" if ((0, 9) == get_min_max([1,4,2,4,2,5,7,0,8,4,9])) else "Fail") #another random list
print ("Pass" if ((0, 0) == get_min_max([0])) else "Fail") #list with only one element
print ("Pass" if ((0, 0) == get_min_max([0,0])) else "Fail") #list with 2 same elements
print ("Pass" if ((0, 9) == get_min_max([0,1,2,3,4,5,6,7,8,9])) else "Fail") #sorted list
print ("Pass" if ((0, 9) == get_min_max([9,8,7,6,5,4,3,2,1,0])) else "Fail") #reversed sorted list
