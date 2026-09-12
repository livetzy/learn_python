from math import sin, cos, tan, radians

def calculate_trig_functions(angle_degrees):
    """Calculate the sine, cosine, and tangent of an angle in degrees."""
    angle_radians = radians(angle_degrees)
    return sin(angle_radians), cos(angle_radians), tan(angle_radians)

values = calculate_trig_functions(45)
print(f"sine : {values[0]}")
print(f"cosine : {values[1]}")
print(f"tangent : {values[2]}")


from math import sqrt

def calculate_square_root(value):
    """Calculate the square root of a given value."""

    while True:
     values = int(input('enter a number to calculate its square root:'))
     return sqrt(values)
    
print(f'square root of {values} is: {calculate_square_root(values)}')

from math import floor, ceil

def round_values(value):
    """Round a value to the nearest integer."""
    return floor(value), ceil(value)

values = round_values(3.5)
print(f'floor and ceil of 3.5 are : {values[0]}')
print(f'floor and ceil of 3.5 are : {values[1]}')