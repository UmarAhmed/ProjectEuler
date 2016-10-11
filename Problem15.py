#P15
import math

def findPaths(n):
    num =  math.factorial(2*n)
    denom = (math.factorial(n))*(math.factorial(n))
    paths = num/denom
    print(paths)

findPaths(20)

