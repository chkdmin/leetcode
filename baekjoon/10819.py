# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline
cache = [0 for _ in range(10)]


def solve(arr):
    ret = 0
    for i in range(len(arr) - 1):
        ret += abs(arr[i] - arr[i + 1])
    return ret


def perm(arr, depth):
    if depth >= len(arr) - 1:
        return solve(arr)

    ret = 0
    for i in range(depth, len(arr)):
        arr[depth], arr[i] = arr[i], arr[depth]
        ret = max(ret, perm(arr, depth + 1))
        arr[i], arr[depth] = arr[depth], arr[i]

    return ret


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(perm(arr, 0))


if __name__ == '__main__':
    main()
