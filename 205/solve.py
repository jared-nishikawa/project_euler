#!/usr/bin/python

import itertools

def base_rep(n,b):
    s = ''
    while n:
        s += str(n%b)
        n /= b
    return s[::-1]

def pad(s, length, char='0'):
    return (length-len(s))*char + s

def get_all(num_dice, num_faces):
    all_reps = []
    for i in range(num_faces**num_dice):
        rep = base_rep(i, num_faces)
        rep = pad(rep, num_dice)
        rep = rep.replace('0', str(num_faces))
        rep = map(int, rep)
        all_reps.append(rep)
    return all_reps

def profile(num_dice, num_faces):
    rolls = get_all(num_dice, num_faces)
    roll_profile = {}
    for roll in rolls:
        S = sum(roll)
        roll_profile[S] = roll_profile[S] + 1 \
                if roll_profile.has_key(S) else 1
    return roll_profile

def pete():
    return profile(9,4)

def colin():
    return profile(6,6)

if __name__ == '__main__':
    C = colin()
    c_total = 6**6
    P = pete()
    p_total = 4**9
    total_prob = 0
    for i in range(9,37):
        p_prob = float(P[i])/p_total
        for n in range(6,i):
            c_prob = float(C[n])/c_total
            total_prob += p_prob * c_prob
    print total_prob


