#!/usr/bin/python

import random

def roll(num_dice, num_faces):
    return sum([random.randint(1, num_faces) for _ in range(num_dice)])

def pete():
    return roll(9, 4)

def colin():
    return roll(6, 6)


if __name__ == '__main__':
    pete_wins = 0
    total = 0
    while 1:
        P = pete()
        C = colin()
        total += 1
        if P > C:
            pete_wins += 1
        print float(pete_wins)/total


