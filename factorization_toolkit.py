
import math
import random
from math import gcd

def trial_division(n, limit=10000):
    """Basic trial division for small factrors"""
    if n % 2 == 0:
        return 2
    for i in range (3, min(limit, int(math.sqrt(n)) + 1), 2):
       if n % i == 0:
           return i
    return None

def pollard_rho(n):
    """Pollard's Rho algorithm - fast factorzation"""
    if n % 2 == 0:
        return 2
    x = random.randint(2, n -1)
    c = random.randint(1, n - 1)
    y = x
    d =1
    f = lambda t: (t * t + c) % n
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
    if d != n:
        return d
    return None

def factor_rsa(n):
    """Factor RSA modulus"""
    print("Factoring " + str(n) + " ... ")
    factor = trial_division(n)
    if factor:
        print("Found factor (trial): " + str(factor))
        return factor
    factor = pollard_rho(n)
    if factor and factor !=  n:
        print("Found factor (Pollard's Rho): " + str(factor))
        return factor

if __name__ == "__main__":
          n = 3233
          print("Prime Factorization Toolkit")
          print("Target: " + str(n))
          p = factor_rsa(n)
          if p:
             q = n // p
             print("p = " + str(p))
             print("q = " + str(q))
             print("Verification: " + str(p) + " * " + str(q) + " = " + str(p * q))
          else:
             print("Factoriization failed")


