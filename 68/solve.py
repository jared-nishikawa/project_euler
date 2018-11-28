import itertools

# outer = x0, x1, x2, x3, x4
# inner = y0, y1, y2, y3, y4

def ismagic(array):
    assert len(array)%2 == 0
    n = len(array)//2
    x = array[:n]
    y = array[n:]
    sums = set()
    for i in range(n):
        s = x[i] + y[i] + y[(i+1)%n]
        sums.add(s)
        if len(sums) == 2:
            return False
    return True

def make_solution(array):
    assert len(array)%2 == 0
    n = len(array)//2
    x = array[:n]
    y = array[n:]
    triples = []
    for i in range(n):
        triple = (x[i], y[i], y[(i+1)%n])
        triples.append(triple)
    m = triples.index(min(triples))
    ts = [triples[(m+i)%n] for i in range(n)]
    s = ()
    for t in ts:
        s += t
    return int(''.join(map(str,s)))

#t = 0
magic = []
n = 10
for perm in itertools.permutations(range(1, n + 1)):
    if ismagic(perm):
        solution = make_solution(perm)
        if len(str(solution)) == 16:
            magic.append(solution)

print(max(magic))


