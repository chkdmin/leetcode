# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n = int(input())
        arr = [0 for _ in range(n)]
        c = n // 2
        prev = c
        for i in range(n):
            print(c, prev, i)
            arr[c] = i + 1
            if i % 2 == 0:
                c, prev = prev // 2, c
                if c > 0 and c % 2 == 0:
                    c -= 1
            else:
                c, prev = (prev + (prev // 2)), c
                if c < n - 1 and c % 2 == 0:
                    c += 1
        print(arr)


if __name__ == '__main__':
    main()
