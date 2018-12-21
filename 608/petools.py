def num_divisors(n):
    # initialize with all 1s
    result = [1]*n
    result[0] = 0
    result[1] = 1

    for p in range(2,n):
        if result[p] == 1:
            k,m = 1,1
            while p**k < n:
                a = 1
                last_m = m
                m = m + 1
                while a*p**k < n:
                    result[a*p**k] //= last_m
                    result[a*p**k] *= m
                    a += 1
                k += 1
    return result

def sum_divisors(n):
    # Initialize with all 1s
    result = [1] * n
    result[0] = 0

    # Loop from 2 to n
    for p in range(2, n):
        # Still 1, must be prime
        if result[p] == 1:
            # Loop over prime powers
            k, m = 1, 1
            while p**k < n:
                last_m = m
                m = m + p**k
                a = 1
                # loop over multiples of prime powers
                while a*p**k < n:
                    result[a*p**k] //= last_m
                    result[a*p**k] *= m
                    a += 1
                k += 1
    return result

# Methodology
# n      = p1**a1 . p2**a2 . ... . pk**ak
# phi(n) = p1**(a1-1)(p1-1) . p2**(a2-1)(p2-1) . ... . pk**(ak-1)(pk-1)
# Go through each prime p, divide by p, multiply by p-1
def totient(n):
    # Initialize with n
    phi = list(range(n))
    phi[0] = 1
    phi[1] = 1
    for p in range(2,n):
        # Still p, must be prime
        if phi[p] == p:
            k = 1
            # for each multiple of p (including p)
            # multiple by (p-1)/p
            while k*p < n:
                phi[k*p] = int(phi[k*p]*(p-1)/p)
                k += 1
    return phi

def prime_sieve(n):
    primes = [2]
    for k in range(2,n):
        prime = True
        for p in primes:
            if k % p == 0:
                prime = False
                break
            if p > k**0.5:
                break
        if prime:
            primes.append(k)
    return primes


if __name__ == '__main__':
    num_div = num_divisors(601)
    print(num_div)
