
#  Math Functions in Python
import math


# CEIL -> Return the ceiling of x, the smallest integer greater than or equal to x. If x is not a float, delegates to x__ceil__(), which should return an Integral value.

x = 10.6
print(math.ceil(x))

# FABS -> Return the absolute(positive) value of x

x = -10
print(math.fabs(x))

# Factorial -> Return the factorial value of x

x = 6
print(math.factorial(x))

# Floor -> Opposite of CEIL Function

x = 13.3
print(math.floor(x))

# FSUM(Iterable) -> Return the sum of a List,Tuple

l = [3,9,2,1,12]
print(math.fsum(l))

# SQRT -> Returns the square root value of x

x = 81
print(math.sqrt(x))