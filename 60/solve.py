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
import itertools

primes = {}
small_primes = []

#threshold = 100000000
small_threshold = 10000
threshold = int(str(small_threshold)*2)
ops = 0

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
    s = str(a) + str(b)
    t = str(b) + str(a)
    ops += 1
    return primes.get(int(s)) and primes.get(int(t))

def check_all(*numbers):
    new = numbers[-1]
    for num in numbers[:-1]:
        if not check(num, new):
            return False
    return True

def maximal_subgraph(graph, i):
    checked = {}
    stack = [i]
    checked[i] = 1
    subgraph = []
    while stack:
        cur = stack.pop()
        subgraph.append(cur)

        nbs = graph[cur]
        for nb in nbs:
            if not checked.get(nb):
                stack.append(nb)
                checked[nb] = 1

    return subgraph, checked

def partition(graph):
    checked = {}
    parts = []
    inds = list(graph.keys())
    j = 0
    i = inds[j]
    while 1:
        m, c = maximal_subgraph(graph, i)
        parts.append(m)
        checked.update(c)

        while checked.get(i):
            j += 1
            if j >= len(inds):
                break
            i = inds[j]

        if j >= len(inds):
            break
    return parts

def clean(graph):
    return {v:graph[v] for v in graph.keys() if graph[v]}

def delete(graph, vxs):

    copy = {v:graph[v].copy() for v in graph}
    for i in vxs:
        copy[i] = {}
    for v in copy.keys():
        for i in vxs:
            if i in copy[v]:
                copy[v].remove(i)
    clean(copy)
    return copy

def min_degree(graph):
    result = 2**64
    for v in graph.keys():
        if len(graph[v]) < result:
            result = len(graph[v])
    return result

def max_degree(graph):
    result = 0
    for v in graph.keys():
        if len(graph[v]) > result:
            result = len(graph[v])
    return result

def degree_check(graph, degree):
    for v in graph.keys():
        if len(graph[v]) < degree:
            return False
    return True

def trim_once(graph, degree):
    # one pass
    for i, v in enumerate(graph):
        if len(v) < degree:
            graph = delete(graph, i)
    return graph

def trim(graph, degree):
    while not degree_check(graph, degree):
        graph = trim_once(graph, degree)
    return graph

def induce(graph, vxs):
    shared_nbs = graph[vxs[0]]
    for vx in vxs:
        shared_nbs = shared_nbs.intersection(graph[vx])

    result = {}
    for v in graph.keys():
        # if v is not one of the pivot vertices
        # and is also not one of the neighbors
        if (v not in vxs) and (v not in shared_nbs):
            continue
        result[v] = graph[v]
        to_remove = []
        for u in result[v]:
            if u not in vxs and u not in shared_nbs:
                to_remove.append(u)
        for u in to_remove:
            result[v].remove(u)

    return result

def is_clique(graph, vxs):
    for u in vxs:
        for v in vxs:
            if v != u and v not in graph[u]:
                return False
    return True

def find_clique(graph, n):
    cliques = []
    for comb in itertools.combinations(graph.keys(), n):
        if is_clique(graph, comb):
            return comb


if __name__ == '__main__':
    get_primes()
    G = {}
    for p in small_primes:
        G[p] = set()
    for p in small_primes:
        for q in small_primes:
            if p < q and check(p,q):
                G[p].add(q)
                G[q].add(p)
    G = clean(G)

    for Z in [3,7,11,13,17,19]:
        subg = induce(G, [Z])
        leftover = delete(subg, [Z])

        print(Z, '-', find_clique(leftover, 4))
        print("*"*20)

