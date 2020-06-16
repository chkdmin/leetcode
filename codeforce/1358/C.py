# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        x1, y1, x2, y2 = map(int, input().split())
        w = x2 - x1 + 1
        h = y2 - y1 + 1
        min_n = min(w, h)
        max_n = max(w, h)
        ret = min_n + ((min_n - 1) * (max_n - min_n + (min_n - 2)))
        print(ret)


if __name__ == '__main__':
    main()
