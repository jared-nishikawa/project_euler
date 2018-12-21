import random

def isprime(n, tests=10):
    if n < 4:
        return True
    for _ in range(tests):
        a = random.randint(2, n-2)
        print(a)
        if pow(a,n-1,n) != 1:
            return False
    return True



