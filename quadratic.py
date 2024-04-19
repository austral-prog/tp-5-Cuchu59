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
    formula = f"f(x) = {a} * X^2 + {b} * X + {c}"
    return formula

def derivation(a, b):
    derivative = f"{2*a}x + {b}" # La cuadratica sola se puede hacer por tabla (gracias a Dios)
    return derivative
