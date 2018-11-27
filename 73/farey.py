def farey_function(n):
    """Print the nth Farey sequence"""
    a, b, c, d = 0, 1, 1, n
    good = 0
    while c <= n:
        k = int((n + b) / d)
        a, b, c, d = c, d, (k*c-a), (k*d-b)
        if a/b > 1/3 and a/b < 1/2:
            good += 1
        if a/b >= 1/2:
            break
    print(good)

farey_function(12000)


