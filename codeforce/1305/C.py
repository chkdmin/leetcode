# -*- coding: utf-8 -*-
import sys
from random import randint

input = sys.stdin.readline


def random():
    n = 2 * (10 ** 5)
    m = 1000
    arr = [randint(1, 999) for _ in range(n)]
    ret = 1
    for i in range(n):
        for j in range(i + 1, n):
            ans = abs(arr[i] - arr[j])
            while ans > m:
                ans -= m

            ret *= ans
            while ret > m:
                ret -= m
        print(i)
    print(ret % m)


def random2():
    n = 2 * (10 ** 3)
    m = 10
    arr = [randint(0, 10 ** 9) for _ in range(n)]
    ret = 1
    for i in range(n):
        for j in range(i + 1, n):
            ret *= abs(arr[i] - arr[j])
        print(i)
    print(ret % m)


def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    ret = 1
    for i in range(n):
        for j in range(i + 1, n):
            ret *= abs(arr[i] - arr[j])
    print(ret % m)


if __name__ == '__main__':
    random()
