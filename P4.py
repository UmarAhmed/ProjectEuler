#P4
"""
A palindromic number reads the same both ways. (727)
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers. 100-999
"""

def pal():
    x = 0
    pal_n = [ ]
    for a in range(100,1000):
        for b in range(100,1000):
            x = str(a*b)
            if x == x[::-1]:
                pal_n.append(int(x))
    y = len(pal_n) - 1
    z = sorted(pal_n)
    print(z[y])
          
               
pal()
