import sys
import fermat

# generate all primes < n
def gen_primes(n):
    for p in range(2,n):
        if fermat.isprime(p):
            print(p)

if __name__ == '__main__':
    if not sys.argv[1:]:
        sys.exit("Need arg")
    n = int(sys.argv[1])
    gen_primes(n)

