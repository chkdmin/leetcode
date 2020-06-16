# -*- coding: utf-8 -*-
import sys

from math import sqrt

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n = int(input())
        arr = []
        for __ in range(n):
            arr.append(list(input().strip()))

        is_no = False
        for i in range(n):
            for j in range(n):
                if arr[i][j] != '1':
                    continue
                if i == n - 1 or j == n - 1:
                    continue

                if arr[i + 1][j] == '0' and arr[i][j + 1] == '0':
                    is_no = True
                    break

            if is_no:
                break
        print('NO' if is_no else 'YES')


if __name__ == '__main__':
    main()
