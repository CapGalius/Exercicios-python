import time
import math

def is_prime_v1(n):
    """Return 'True' if number is a prime number. False otherwise"""
    if n == 1:
        return False # 1 is not prime

    for d in range(2, n):
        if n % d == 0:
            return False
    return True

#=======Time Function ========
t0 = time.time()
for n in range(1, 100000):
    print(n, is_prime_v1(n))
    is_prime_v1(n)
t1= time.time()
timeV1 = t1-t0


def is_prime_v2(n):
    """Return 'True' if number is a prime number. False otherwise"""
    if n == 1:
        return False # 1 is not prime
    
    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True

#=======Time Function ========
t0 = time.time()
for n in range(1, 100000):
    print(n, is_prime_v2(n))
    is_prime_v2(n)
t1= time.time()
timeV2 = t1-t0



def is_prime_v3(n):
    """Return 'True' if number is a prime number. False otherwise"""
    if n == 1:
        return False # 1 is not prime
    # If its even (par) and not 2, it's not prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True

#=======Time Function ========
t0 = time.time()
for n in range(1, 100000):
    print(n, is_prime_v3(n))
    is_prime_v3(n)
t1= time.time()
timeV3 = t1-t0

print("Time required V1:", timeV1)
print("Time required V2:", timeV2)
print("Time required V3:", timeV3)