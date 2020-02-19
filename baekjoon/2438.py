# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    n = int(input())
    for i in range(1, n + 1):
        print(' ' * (n - i), end='')
        print('*' * i)


if __name__ == '__main__':
    main()
