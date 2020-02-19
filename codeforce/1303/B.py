# -*- coding: utf-8 -*-
import sys

import math

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n, g, b = map(int, input().split())
        if n <= g:
            print(n)
            continue

        good = math.ceil(n / 2)
        bad = n - good
        ret = 0

        # good 빼기
        if good >= g:
            good -= g
            ret += g
        else:
            good = 0
            ret += good

        # bad 빼기
        if bad >= b:
            bad -= b
        else: # Pass
            bad = 0
        ret += b

        print(ret)





if __name__ == '__main__':
    main()
