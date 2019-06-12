def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    return rotated_array_search_recusive(input_list, number, 0, len(input_list) - 1)

def rotated_array_search_recusive(input_list, number, min, max):
    if min > max:
        return -1

    center = min + (max - min) // 2

    if input_list[center] == number:
        return center

    if input_list[min] < input_list[center]: #no rotation until here
        if number < input_list[center] and number >= input_list[min]: #if number is smaller and is in left range, go left
            max = center - 1
        else: #if number is bigger or not in left range, go right
            min = center + 1
    else: #rotated array!
        if number < input_list[center]: #searched number is smaller than element at center
            if input_list[max] > number: # go left
                max = center - 1
            else: # go right
                min = center + 1
        else: #searched number is bigger than element at center
            if input_list[max] < number: # go left
                max = center - 1
            else: # go right
                min = center + 1

    return rotated_array_search_recusive(input_list, number, min, max)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

test_function([[1], 1]) #test input with only one element and existing number
test_function([[], 1]) #test empty input
test_function([[1], 2]) #test input with only one element and nonexisting number
