def phi_sieve(n):
    # phi of 0 1 2
    phi = list(range(n))
    phi[0] = 1
    phi[1] = 1
    for p in range(2,n):
        # Not initialized, must be prime
        if phi[p] == p:
            k = 1
            while k*p < n:
                phi[k*p] = int(phi[k*p]*(p-1)/p)
                k += 1
    return phi

if __name__ == '__main__':

    phi = phi_sieve(1000001)

    n = 1000000
    print(sum(phi[i] for i in range(2,n+1)))
