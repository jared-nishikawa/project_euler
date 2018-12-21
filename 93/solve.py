import itertools
import string
import math



'''
"." represents any operation (+-*/)
expression
a . b . c . d

parenthesis templates
a.((b.c).d)
(a.(b.c)).d
(a.b).(c.d)
((a.b).c).d
a.(b.(c.d))
'''

templates = [
        "x = {a}{op1}(({b}{op2}{c}){op3}{d})",
        "x = ({a}{op1}({b}{op2}{c})){op3}{d}",
        "x = ({a}{op1}{b}){op2}({c}{op3}{d})",
        "x = (({a}{op1}{b}){op2}{c}){op3}{d}",
        "x = {a}{op1}({b}{op2}({c}{op3}{d}))"]

ops = "+-*/"

def results(comb):
    nums = set()
    for op in itertools.product(ops, repeat=3):
        for perm in itertools.permutations(comb, 4):
            args = {
                    'a': perm[0],
                    'b': perm[1],
                    'c': perm[2],
                    'd': perm[3],
                    'op1': op[0],
                    'op2': op[1],
                    'op3': op[2]}
    
            for template in templates:
                data = {}
                expr = template.format(**args)
                try:
                    exec(expr, None, data)
                except:
                    continue
                x = data['x']
                if x == int(x) and x > 0:
                    nums.add(int(x))
    return sorted(list(nums))

def length_run(nums):
    length = 0
    for ind, num in enumerate(nums):
        if num != ind+1:
            break
        length += 1
    return length

if __name__ == '__main__':
    digits = string.digits
    
    combs = [comb for comb in itertools.combinations(digits, 4)]

    best = 0
    winner = None
    
    for comb in combs:
        nums = results(comb)
        l = length_run(nums)
        if l > best:
            winner = comb
            best = l
    print(best)
    print(winner)
    
