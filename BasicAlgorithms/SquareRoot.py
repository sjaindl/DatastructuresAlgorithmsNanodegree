def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    
    if number < 2:
        return number

    smaller_number = sqrt(number >> 2) << 1
    larger_number = smaller_number + 1
    if larger_number * larger_number > number:
        return smaller_number
    return larger_number

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

print ("Pass" if  (1 == sqrt(1)) else "Fail") #test small number
print ("Pass" if  (32 == sqrt(1024)) else "Fail") #test binary number
print ("Pass" if  (999 == sqrt(998001)) else "Fail") #test large number
