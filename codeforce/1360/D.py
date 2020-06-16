# -*- coding: utf-8 -*-
import sys

from math import sqrt

input = sys.stdin.readline


def get_divisor(n):
    ret = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            ret.add(i)
            ret.add(n // i)
    return sorted(ret)


def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        if k >= n:
            print(1)
            continue
        arr = get_divisor(n)
        ret = -1
        for num in arr:
            if num > k:
                break
            ret = num
        print(n // ret)


if __name__ == '__main__':
    main()
