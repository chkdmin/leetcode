# -*- coding: utf-8 -*-
import random
import string
import sys
from collections import Counter

input = sys.stdin.readline


def main():
    n, m, k = map(int, input().split())
    pos = []
    ans = ''
    my = mx = 0
    for _ in range(k):
        pos.append(list(map(int, input().split())))
    for idx in range(k):
        dy, dx = map(int, input().split())
        cy, cx = pos[idx]
        cy += my
        if cy < 0:
            cy = 0
        elif cy > n:
            cy = n

        cx += mx
        if cx < 0:
            cx = 0
        elif cx > m:
            cx = m

        if dy > cy:
            ans += ('D' * (dy - cy))
            my += (dy - cy)
        elif dy < cy:
            ans += ('U' * (cy - dy))
            my -= (cy - dy)
        if dx > cx:
            ans += ('R' * (dx - cx))
            mx += (dx - cx)
        elif dx < cx:
            ans += ('L' * (cx - dx))
            mx -= (cx - dx)
    print(len(ans))
    print(ans)


if __name__ == '__main__':
    main()
