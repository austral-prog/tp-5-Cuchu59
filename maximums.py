def max_of_two(x, y):
    max_value = 0
    if(x >= y):
        max_value = x
    else:
        max_value = y
    return max_value

def max_of_three(x,y,z):
    return max_of_two(x,y) if max_of_two(x,y) >= max_of_two(y,z) else max_of_two(y,z)
