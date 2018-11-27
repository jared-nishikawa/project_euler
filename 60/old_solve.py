"""
The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in
any order the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum
for a set of four primes with this property.

Find the lowest sum for a set of five primes for which
any two primes concatenate to produce another prime.
"""

import time

primes = {}
small_primes = []

threshold = 19992000
small_threshold = 2000
ops = 0

graph = {}

def get_primes():
    global primes
    with open('../primes.txt') as f:
        for line in f:
            prime = int(line)
            if prime < small_threshold:
                small_primes.append(prime)
            if prime > threshold:
                break
            primes[prime] = 1

def check(a, b):
    global ops
    if graph.get(a) and graph.get(a).get(b):
        return True

    s = str(a) + str(b)
    t = str(b) + str(a)
    ops += 1
    result = primes.get(int(s)) and primes.get(int(t))
    if result:
        graph[a] = {**graph.get(a, {}), **{b:1}}
        graph[b] = {**graph.get(b, {}), **{a:1}}

    return result

def check_all(*numbers):
    new = numbers[-1]
    for num in numbers[:-1]:
        if not check(num, new):
            return False
    return True

if __name__ == '__main__':
    start = time.time()
    get_primes()
    end_setup = time.time()
    print("Setup: %.2fs" % (end_setup-start))

    main = time.time()
    concats = [[], [], [], []]

    op_check = 0

    for p in small_primes:
        for q in small_primes:
            if p != q:
                if check(p,q):
                    concats[0].append((p,q))

    print("Ops (round 0):", ops-op_check)
    op_check = ops

    for i in range(0,3):
        for r in small_primes:
            for nums in concats[i]:
                if r not in nums:
                    if check_all(*nums, r):
                        concats[i+1].append(list(nums) + [r])
        print(f"Ops (round {i+1}):", ops-op_check)
        op_check = ops

    print([m for m in map(len, concats)])

    print("Threshold:", threshold)
    print("Small threshold:", small_threshold)
    print("Num small primes:", len(small_primes))
    print("Ops:", ops)
    end = time.time()
    print("Main: %.2fs" % (end-main))
    print("Total: %.2fs" % (end-start))


    print("*"*20)
    for c in concats:
        if c:
            print(min(map(sum, c)))
        else:
            print("No data")
