# Efficient solutions to problems
from functools import reduce
import math


# This function returns all primes numbers <= n
# Helpful for many problems
def primes_sieve(n):
    primes = dict()
    for i in range(2, n + 1):
        primes[i] = True

    for i in primes:
        factors = range(i, n + 1, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i] is True]


# Euclidean GCD Function (can define onto an array by chaining)
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# Simple LCM function in terms of GCD
def lcm(a, b):
    return (a * b) // gcd(a, b)


# Returns nCk using multiplicative formula
def choose(n, k):
    product = 1
    for i in range(1, k + 1):
        product *= (n + 1 - i)//i
    return product


# Problem 1
# Find the sum of all the multiples of 3 or 5 below 1000.
def p1(n=1000):
    return sum([i for i in range(1, n) if i % 5 == 0 or i % 3 == 0])


# Problem 2
# By considering the terms in the Fibonacci sequence whose values do not exceed four million
# Find the sum of the even-valued terms.
# We use a simple iterative approach (recursive with memoization is also good)
def p2(n=4000000):
    f1, f2 = 1, 2
    even_sum = 0
    while f2 < n:
        if f2 % 2 == 0:
            even_sum += f2
        f1, f2 = f2, f1 + f2
    return even_sum


# Problem 3
# What is the largest prime factor of the number 600851475143 ?
def p3(n=600851475143):
    i = 2
    while i**2 <= n:  # largest factor of a number to check is its sq. rt.
        if n % i == 0:
            n = n // i
        else:
            i += 1
    return n


# Problem 4
# Find the largest palindrome made from the product of two 3-digit numbers.
# We note that all even-length palindromes are divisible by 11
# This function returns the max palindrome between low and high
# But could be altered to optimize this specific case
def p4(low=100, high=999):
    maximum = 0
    for i in range(low, high + 1):
        for j in range(i + 1, high + 1):
            if i * j > maximum and str(i * j) == str(i * j)[::-1]:
                maximum = max(i * j, maximum)
    return maximum


# Problem 5
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def p5():
    array = [11, 13, 14, 16, 17, 18, 19, 20]
    i = 0
    current = 20
    while i != len(array):
        if current % array[i] == 0:
            i += 1
        else:
            current += 20
            i = 0
    return current


# Much faster solution to problem 5
# Note LCM was defined near the top of this file
def alternate_p5(n):
    return reduce(lcm, range(1, n + 1), 1)


# Problem 6
# Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum.
# This function uses summation formulae to find the answer
def p6(n):
    sq_sum = n*(n+1)*(2*n+1) // 6
    sum_sq = ((n**2 + n) // 2)**2
    return sum_sq - sq_sum


# Problem 7
# What is the 10, 001st prime number?
# We use our previously defined sieve and the prime distribution
def p7(n):
    a = n
    while a // math.log(a) < n:
        a += 10
    return len(primes_sieve(a))


# Problem 8
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# Included below is the 1000-digit number in string-form as seq
def p8():
    seq = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    seq = [int(i) for i in seq]
    m_p = reduce((lambda x, y: x * y), seq[: 13])
    for i in range(1, len(seq) - 13):
        if i != 0:
            product = reduce((lambda x, y: x * y), seq[i:i + 13])
            m_p = max(product, m_p)
    return m_p


# Problem 9
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the value of abc
# We use the equations: a + b + c = 1000, a < b < c, a**2 + b**2 = c**2
def p9():
    for a in range(1, 1001):
        for b in range(a + 1, 1001):
            if a**2 + b**2 == (1000 - a - b)**2:
                return a * b * (1000 - a - b)


# Problem 10
def p10():
    return sum(primes_sieve(2000000))



