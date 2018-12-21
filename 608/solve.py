from petools import num_divisors

def D():
    num_div = num_divisors(601)
    divs = [1,2,3,6]
    n = 100

    total = [num_div[k*d] for k in range(1, n+1) for d in divs]
    print(sum(total))

D()
