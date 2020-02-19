# -*- coding: utf-8 -*-
import sys

import math

input = sys.stdin.readline


def lcm(a, b):
    return a * b / math.gcd(a, b)


def main():
    X = int(input())
    smallest = 10 ** 12
    ret = None
    for n in range(1, int(math.sqrt(X)) + 1):
        if X % n == 0:
            n1, n2 = n, X // n
            if lcm(n1, n2) != X:
                continue
            smallest = min(smallest, max(n1, n2))
            ret = n, X // n
    print(ret[0], ret[1])


if __name__ == '__main__':
    main()
