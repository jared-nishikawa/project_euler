def sum_divisors(n):
    """Return a list of the sums of divisors for the numbers below n.

    >>> sum_divisors(10) # https://oeis.org/A000203
    [0, 1, 3, 4, 7, 6, 12, 8, 15, 13]

    """
    result = [1] * n
    result[0] = 0
    for p in range(2, n):
        if result[p] == 1: # p is prime
            p_power, last_m = p, 1
            while p_power < n:
                m = last_m + p_power
                for i in range(p_power, n, p_power):
                    result[i] //= last_m    # (B)
                    result[i] *= m          # (B)
                last_m = m
                p_power *= p
    return result

N = 1000001

sum_div = sum_divisors(N)

checked = [0]*N

def gen_chain(k):
    chain = [k]
    if k >= N:
        return 1, chain
    #checked[k] = 1
    _set = set()
    _set.add(k)
    while 1:
        cur = chain[-1]
        nxt = sum_div[cur] - cur
        if nxt >= N:
            return 1, chain
        #checked[nxt] = 1

        if nxt == 0:
            return 1, chain

        if nxt == k:
            return 0, chain

        if nxt in _set:
            return 1, chain

        chain.append(nxt)
        _set.add(nxt)

if __name__ == '__main__':
    chains = []
    i = 1
    while 1:
        err, chain = gen_chain(i)
        checked[i] = 1
        if not err:
            chains.append((len(chain), min(chain)))
        while i < N and checked[i]:
            i += 1
        if i >= N:
            break

    print(sorted(chains))
