# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    m = 0
    for idx, num in enumerate(arr):
        if num > m:
            pass


if __name__ == '__main__':
    main()
