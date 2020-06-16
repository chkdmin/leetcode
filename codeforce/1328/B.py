# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        n1 = n2 = 0
        for i in range(2, n + 1):
            if k <= (i * (i - 1)) / 2:
                n1 = i - 1
                n2 = n1 - (((n1 * (n1 + 1)) // 2) - k) - 1
                break
        i = n - n1 - 1
        j = n - n2 - 1
        print(('a' * i) + 'b' + ('a' * (j - i - 1)) + 'b' + ('a' * (n - j - 1)))


if __name__ == '__main__':
    main()
