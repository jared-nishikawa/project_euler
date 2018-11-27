'''compute continued fraction of square root'''

from math import sqrt

def continued(n):
    z = x = m = 1
    while n > m**2:
        m += 1
    c = m-1
    m = y = m-1
    l = ()
    while -z < x:
        x = (n-y*y)//x
        y += m
        l += (y//x,)

        y = m-y%x
        z = -1
    return c, l

def solve_pell(n):
    a0,a = continued(n)
    L = len(a)

    nums = []
    denoms = []

    for x,y in ((a0,1), (a[0]*a0+1, a[0])):
        if x**2 - n*y**2 == 1:
            return x,y

        nums.append(x)
        denoms.append(y)

    i = 1
    while 1:
        num = nums[-1]*a[i%L] + nums[-2]
        denom = denoms[-1]*a[i%L] + denoms[-2]
        i += 1
        nums.append(num)
        denoms.append(denom)
        x = num
        y = denom
        if x**2 - n*y**2 == 1:
            return x,y
        del nums[0]
        del denoms[0]

maxx = 0
D = 0
for i in range(1, 1000):
    x,y = solve_pell(i)
    if x > maxx:
        maxx = x
        D = i

print(maxx, D)


