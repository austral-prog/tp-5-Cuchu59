def max_of_two(x, y):
    max_value = 0
    if(x >= y):
        max_value = x
    else:
        max_value = y
    return max_value

def max_of_three(x,y,z):
    max_value = 0
    if(x >= y and x >= z):
        max_value = x
    elif(y >= x and y >= z):
        max_value = y
    else:
        max_value = z
    return max_value
