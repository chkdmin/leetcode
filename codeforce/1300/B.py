# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        print(arr[n] - arr[n - 1])


if __name__ == '__main__':
    main()
