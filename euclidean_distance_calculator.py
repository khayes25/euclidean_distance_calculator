"""
@author: Keon Hayes
"""

import math #Importing the math module to use its square root function.

"""
The input function will print "Enter the first point's x-coordinate (x1): "
and wait for the user to type their entry.
When the user presses the "Enter" key on their keyboard,
the value they typed will be returned as a string-type to the x1 variable,
and immediately typecast as a float.
"""

x1 = float(input("Enter the first point's x-coordinate (x1): "))

"""
The input function will print "Enter the first point's y-coordinate (y1): "
and wait for the user to type their entry.
When the user presses the "Enter" key on their keyboard,
the value they typed will be returned as a string-type to the y1 variable,
and immediately typecast as a float.
"""

y1 = float(input("Enter the first point's y-coordinate (y1): "))

"""
The input function will print "Enter the second point's x-coordinate (x2): "
and wait for the user to type their entry.
When the user presses the "Enter" key on their keyboard,
the value they typed will be returned as a string-type to the x2 variable,
and immediately typecast as a float.
"""

x2 = float(input("Enter the second point's x-coordinate (x2): "))

"""
The input function will print "Enter the second point's y-coordinate (y2): "
and wait for the user to type their entry.
When the user presses the "Enter" key on their keyboard,
the value they typed will be returned as a string-type to the y2 variable,
and immediately typecast as a float.
"""

y2 = float(input("Enter the second point's y-coordinate (y2) : "))

"""
The Euclidean Distance formula will be calculated using the values of the x1,
x2, y1, and y2 variables. The result of this calculation will be printed to the user.
"""

print("The distance between your two points is ", math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), ".", sep="")
