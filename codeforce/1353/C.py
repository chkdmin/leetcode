# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n = int(input())
        if n == 1:
            print(0)
            continue

        ret = 8
        s = 2
        for c in range(5, n + 1, 2):
            ret += (c * 2 + (c - 2) * 2) * s
            s += 1
        print(ret)


if __name__ == '__main__':
    main()
