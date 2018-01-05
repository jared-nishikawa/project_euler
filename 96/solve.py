#!/usr/bin/python

def read_file():
    with open('p096_sudoku.txt') as f:
        lines = map(lambda x: list(x.strip()), f.readlines())
        puzzles_str = [lines[i*10+1:i*10+10] for i in range(50)]
        puzzles = []
        for puzzle in puzzles_str:
            new_puzzle = map(lambda x: map(int, x), puzzle)
            puzzles.append(new_puzzle)

    return puzzles

def list_copy(L):
    new = []
    for item in L:
        if type(item) == list:
            new.append(list_copy(item))
        else:
            new.append(item)
    return new

def solved(puzzle):
    is_solved = True
    for line in puzzle:
        if 0 in line:
            return False
    return True

def naive_solve(puzzle):
    while 1:
        changed = 0
        for i in range(9):
            for j in range(9):
                if P[i][j] == 0:
                    sieve(P)
                    changed += elimination(P, i, j)
        if not changed:
            break

def sieve(puzzle):
    for k in range(1,10):
        sieve_k(puzzle, k)

def sieve_k(puzzle, k):
    blackout = list_copy(puzzle)
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == k:

                for l in range(9):
                    # Black out horiz
                    blackout[l][j] = -1

                    # Black out vert
                    blackout[i][l] = -1

                # Black out box
                X = i/3
                Y = j/3
                for x in range(3*X, 3*X+3):
                    for y in range(3*Y, 3*Y+3):
                        blackout[x][y] = -1


    for i in range(9):
        for j in range(9):
            if blackout[i][j] != 0:
                continue

            # Horizontal
            horiz = [blackout[l][j] for l in range(9)]
            if horiz.count(0) == 1:
                puzzle[i][j] = k

            # Vertical
            vert = [blackout[i][l] for l in range(9)]
            if vert.count(0) == 1:
                puzzle[i][j] = k

            # Box
            X = i/3
            Y = j/3
            box = [blackout[x][y] for x in range(3*X,3*X+3) \
                    for y in range(3*Y, 3*Y+3)]
            if box.count(0) == 1:
                puzzle[i][j] = k

def elimination(puzzle, x, y):
    possible = [1,2,3,4,5,6,7,8,9]

    # Horizontal
    for i in range(9):
        if i == x:
            continue
        if puzzle[i][y] != 0:
            try:
                possible.remove(puzzle[i][y])
            except:
                pass

    # Vertical
    for i in range(9):
        if i == y:
            continue
        if puzzle[x][i] != 0:
            try:
                possible.remove(puzzle[x][i])
            except:
                pass

    # Box
    X = x/3
    Y = y/3

    for i in range(3*X, 3*X+3):
        for j in range(3*Y, 3*Y+3):
            if puzzle[i][j] != 0:
                try:
                    possible.remove(puzzle[i][j])
                except:
                    pass
    if len(possible) == 1:
        puzzle[x][y] = possible[0]
        return 1

    return 0

if __name__ == '__main__':
    puzzles = read_file()
    num_solved = 0
    for P in puzzles:
        naive_solve(P)
        for line in P:
            print line
        raw_input()
        num_solved += solved(P)
    print num_solved
