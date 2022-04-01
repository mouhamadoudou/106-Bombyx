#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## main.py
## File description:
## main
##

import sys
from math import *
from array import array

arg = sys.argv

def display_h():
    print("USAGE\n    /106bombyx n [k | i0 i1]\n")
    print("DESCRIPTION")
    print("    n    number of first generation individuals\n")
    print("    k    growth rate from 1 to 4\n")
    print("    i0   initial generation (included)\n")
    print("    i1   final generation (included)\n")

def gett(argv):
    result = float(argv)
    return result

def gett_i(argv):
    result = int(argv)
    return result

def start_2(n, i0, i1, u):
    pi = 0
    rn = 0
    k = 1.00

    while u != 4:
        k += 0.01
        pi = n
        for i in range(1, i0):
            rn = k * xp * ((1000.0 -pi) / 1000.0)
            pi = rn
            for z in range(1, (i1 + 1)):
                if xi > 0:
                    print(k, rn)
                else:
                    print(k, 0.00)
                xn = k * pi * ((1000.0 - pi) / 1000.0)
                pi = rn;
        u = u + 1;

def start(k, pi):
    rn = 0.0
    pi = pi * 1.0001
    i = 1.00
    a = 2
    b = 0

    print(1, "%.2f" %pi)
    while a < 101:
        rn = k * pi * ((1000.0 - pi) / 1000.0)
        pi = rn
        if pi > 0:
            print(a, "%.2f" %rn)
        else:
            print(k, a)
        a = a + 1

def main(args):

    if (len(args) == 3):
        start(gett(args[2]), gett(args[1]));
    else:
        start_2(gett(args[1]), gett_i(args[2]), gett_i(args[3]), 0)
    return (0)

if __name__ == '__main__':
    main(arg)
