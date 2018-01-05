#!/usr/bin/python

class Tree(object):
    def __init__(self, n):
        self.n = n
        self.checked = {}
        self.start = bin(n)[2:]
        self.checked[self.start] = True

    def traverse(self, string=None):
        if not string:
            string = self.start
        for i,char in enumerate(string):
            if char == '0':
                prev = string[i-1]
                L = list(string)
                if prev == '0':
                    continue
                if prev == '1':
                    L[i-1] = '0'
                elif prev == '2':
                    L[i-1] = '1'
                L[i] = '2'
                if L[0] == '0':
                    L = L[1:]
                new_string = ''.join(L)
                if not self.checked.has_key(new_string):
                    self.checked[new_string] = True
                    self.traverse(new_string)

if __name__ == '__main__':
    T = Tree(18)
    T.traverse()
    print len(T.checked)


