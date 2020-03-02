# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def get_next_permutation(arr):
    i = j = len(arr) - 1
    while i >= 0:
        if arr[i] > arr[i - 1]:
            i -= 1
            break
        i -= 1

    if i == -1:
        return -1

    while j > i:
        if arr[j] > arr[i]:
            break
        j -= 1

    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j = len(arr) - 1
    while j > i:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return arr


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr = get_next_permutation(arr)
    if arr == -1:
        print(-1)
        return

    for num in arr:
        print(num, end=' ')


if __name__ == '__main__':
    main()
