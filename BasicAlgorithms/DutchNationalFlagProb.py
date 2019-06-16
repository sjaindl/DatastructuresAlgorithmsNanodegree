def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    
    left_ptr = 0 #pos of last 0
    right_ptr = len(input_list) - 1 #pos of last 2
    center_ptr = 0

    while center_ptr <= right_ptr:
        digit = input_list[center_ptr]

        if digit == 0:
            input_list[left_ptr], input_list[center_ptr] = input_list[center_ptr], input_list[left_ptr]
            left_ptr += 1
            center_ptr += 1
        elif digit == 1:
            center_ptr += 1
        else: # digit == 2
            input_list[right_ptr], input_list[center_ptr] = input_list[center_ptr], input_list[right_ptr]
            right_ptr -= 1


    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]) # test some random sequence
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]) # test long sequence
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) # sorted long sequence
test_function([0, 1, 2]) # sorted short sequence
test_function([2, 1, 0]) # reversed sequence
test_function([]) # empty input
test_function([2, 2, 1, 1]) # test only 1 & 2 input
test_function([0, 0, 2, 2]) # test only 0 & 2 input
