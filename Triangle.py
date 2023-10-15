"""Module providing a function printing python version."""

def classify_triangle(a,b,c):
    """Function classifying triangles using their side lengths"""
    # require that the input values be >= 0 and <= 200
    if a >= 200 or b >= 200 or c >= 200:
        return 'InvalidInput'
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput'

    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
# now we know that we have a valid triangle
    if a == b and b == c:
        return 'Equilateral'
    elif ((a ** 2) +(b ** 2)) == (c ** 2) or \
         ((b ** 2) +(c ** 2)) == (a ** 2) or \
         ((c ** 2) +(a ** 2)) == (b ** 2):
        return 'Right'
    elif (a != b) and (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isosceles'
