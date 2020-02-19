# -*- coding: utf-8 -*-
import sys
from bisect import bisect

import math

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n, x = map(int, input().split())
        arr = list(map(int, input().split()))
        big = max(arr)
        if big == x:
            print(1)
            continue
        if big > x:
            print(2)
            continue

        i = 1
        ret = -1
        while i * i <= x:
            if x % i == 0:
                if big >= i:
                    ret = x // i
                    if big == i:
                        break
                if big >= x // i:
                    ret = i
                    if big == x // i:
                        break
            i += 1
        print(ret)


if __name__ == '__main__':
    main()
