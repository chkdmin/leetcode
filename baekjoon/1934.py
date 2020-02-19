# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        a, b = map(int, input().split())
        big = max(a, b)
        small = min(a, b)
        while big % small > 0:
            small, big = (big % small), small
        print(a * b // small)


if __name__ == '__main__':
    main()
