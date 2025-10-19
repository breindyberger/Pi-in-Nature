import random
import time

MAX = 1000000000000000

# returns the greatest common divisor of m and n
# See http://en.wikipedia.org/wiki/Euclidean_algorithm for an explanation
def gcd(m, n):
    if n == 0: return m
    else: return gcd(n, m % n)

before = time.time()

for i in range(100):
    num1 = random.randint(0, MAX)
    num2 = random.randint(0, MAX)
    gcd(num1, num2)


