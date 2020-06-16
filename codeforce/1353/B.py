# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        a = sorted(map(int, input().split()))
        b = sorted(map(int, input().split()))
        for c in range(k):
            i = c
            j = len(b) - (1 + c)
            if a[i] >= b[j]:
                break
            a[i], b[j] = b[j], a[j]
        print(sum(a))


if __name__ == '__main__':
    main()
