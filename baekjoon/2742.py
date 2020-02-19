# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    n = int(input())
    for i in range(n, 0, -1):
        print(i)


if __name__ == '__main__':
    main()
