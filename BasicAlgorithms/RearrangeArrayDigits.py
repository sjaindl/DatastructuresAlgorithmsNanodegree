from queue import PriorityQueue

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    pq = PriorityQueue() #this is a min priority queue

    for element in input_list:
        pq.put(element)

    left = ""
    right = ""

    while pq.qsize() > 1:
        right = str(pq.get()) + right
        left = str(pq.get()) + left

    if pq.qsize() == 1:
        left = str(pq.get()) + left

    if left == "":
        left = 0
    if right == "":
        right = 0

    return [int(left), int(right)]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_case = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case)

test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

test_case = [[], [0, 0]] #test empty input
test_function(test_case)

test_case = [[0], [0, 0]] #test zero input
test_function(test_case)

test_case = [[1], [0, 1]] #test input with only one digit
test_function(test_case)

test_case = [[4, 6, 2, 5, 9, 8, 1, 3, 3, 9, 8, 7, 2], [9986432, 875321]] #test large input
test_function(test_case)
