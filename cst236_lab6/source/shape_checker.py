"""
:mod:`source.source1` -- Example source code
============================================

The following example code determines if a set of 3 sides of a triangle is equilateral, scalene or iscoceles
"""

def get_triangle_type(a=0, b=0, c=0):
    """
    Determine if the given triangle is equilateral, scalene or Isosceles

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float

    :param c: line c
    :type c: float

    :return: "equilateral", "isosceles", "scalene" or "invalid"
    :rtype: str
    """
    if isinstance(a, (tuple, list)) and len(a) == 3:
        c = a[2]
        b = a[1]
        a = a[0]

    if isinstance(a, dict) and len(a.keys()) == 3:
        values = []
        for value in a.values():
            values.append(value)
        a = values[0]
        b = values[1]
        c = values[2]

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0:
        return "invalid"

    if a == b and b == c:
        return "equilateral"

    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"

def get_quadrilateral_type(a=0, b=0, c=0, d=0, c1=0, c2=0, c3=0, c4=0):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)) and isinstance(d, (int, float))):
        return "invalid"
    if not (isinstance(c1, (int, float)) and isinstance(c2, (int, float)) and isinstance(c3, (int, float)) and isinstance(c4, (int, float))):
        return "invalid"

    if c1 == 90 and c2 == 90 and c3 == 90 and c4 == 90:
        if a == b and b == c and c == d:
            return "square"
        elif a == c and b == d:
            return "rectangle"
        else:
            return "disconnected"


    sum_of_angles = c1+c2+c3+c4
    if sum_of_angles != 360:
        return "disconnected"

    if (c1 == c3 and c2 == c4) and (c1 != c2 and c3 != c4):
        if a == b and b == c and c == d:
            return "rhombus"
        else:
            return "disconnected"
    
  
     

    
    
    











