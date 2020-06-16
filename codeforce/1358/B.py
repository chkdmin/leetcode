# -*- coding: utf-8 -*-
import sys
from collections import Counter

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n = int(input())
        r = 1
        arr = sorted(list(map(int, input().split())))
        c = 0
        for n in arr:
            if n <= (r + c):
                r += (c + 1)
                c = 0
            else:
                c += 1
        print(r)


if __name__ == '__main__':
    main()
