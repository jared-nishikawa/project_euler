import itertools
primes = []
threshold = 5
with open('../primes.txt') as f:
    for line in f:
        prime = int(line)
        if len(primes) > threshold:
            break
        primes.append(prime)

print(primes)


counter = 0
for i in range(len(primes) + 1):
    for comb in itertools.combinations(primes, i):
        print(comb)
        counter += 1

print(counter)

