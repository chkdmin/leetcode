# -*- coding: utf-8 -*-
import sys
from random import randint

import itertools

input = sys.stdin.readline


def solve(arr):
    meta = {}
    for i in range(len(arr)):
        idx = meta.get(i - arr[i], None)
        if idx is not None:
            meta[i - arr[i]] = None
            arr[idx], arr[i] = arr[i], arr[idx]
            meta[idx - arr[idx]] = idx
        meta[i - arr[i]] = i
    return arr


def is_good(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if i - arr[i] == j - arr[j]:
                return False
    return True


def main():
    for _ in range(int(input())):
        n = randint(1, 10)
        arr = [randint(1, 10) for _ in range(n)]
        print(n, arr, is_good(arr))
        arr = solve(arr)
        print(n, arr, is_good(arr))
        end = n // 2
        start = 0
        while start < end:
            arr.append(arr.pop(start))
            start += 1
        print(n, arr, is_good(arr))
        for per in itertools.permutations(arr):
            if is_good(per):
                print(n, per, is_good(per))
                break
        print('-' * 100)


if __name__ == '__main__':
    main()
