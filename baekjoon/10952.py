# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        print(a + b)


if __name__ == '__main__':
    main()
