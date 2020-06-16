import sys

import math

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        a, b, c, d = map(int, input().split())
        x, y, x1, y1, x2, y2 = map(int, input().split())
        if (a != 0 or b != 0) and x1 == x2:
            print('No')
            continue
        if (c != 0 or d != 0) and y1 == y2:
            print('No')
            continue
        if a >= b:
            a -= b
            b = 0
            if a > x - x1:
                print('No')
                continue
        else:
            b -= a
            a = 0
            if b > x2 - x:
                print('No')
                continue
        if c >= d:
            c -= d
            d = 0
            if c > y - y1:
                print('No')
                continue
        else:
            d -= c
            c = 0
            if d > y2 - y:
                print('No')
                continue
        print('Yes')


if __name__ == '__main__':
    main()
