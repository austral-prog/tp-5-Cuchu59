def roots(a, b, c):
    import math

    roots = [0, 0] # Como tiene 2 raices es preferible tener una sola variable que los almaceneÑ roots[0] y roots[1]
    
    if( (b*b) - (4*a*c) >= 0 ):
        second_term = math.sqrt((b*b) - (4*a*c))
    else:
        return f"( )"
    
    # En una raiz sumo y en la otra resto, definiendo los valores dentro de roots
    roots[0] = (-b + second_term)/2*a
    roots[1] = (-b - second_term)/2*a
    
    if(roots[0] == roots[1]):
        return f"({roots[1]})"
        
    return f"({roots[0]}, {roots[1]})"



def value_y(a, b, c, x):
    y = 0
    y = a*x*x + b*x + c
    return y

def to_string(a, b, c):
    formula = f"f(x) ="
    if(a != 0):
        term1 =  f" {a} * X^2 +"
        formula = formula + term1
    if(b != 0):
        term2 = f" {b} * X +"
        formula = formula + term2
    if(c != 0):
        term3 = f" {c}"
        formula = formula + term3
    
    return formula

def derivation(a, b, c):
    formula = f"f'(x) ="
    if(a != 0):
        term1 =  f" {a*2} * X"
        formula = formula + term1
    if(b != 0 and a != 0):
        term2 = f" + {b}"
        formula = formula + term2
    elif(a == 0 and b != 0):
        term2 = f" {b}"
        formula = formula + term2
    return formula
