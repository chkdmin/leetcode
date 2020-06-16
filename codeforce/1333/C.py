# -*- coding: utf-8 -*-
import random
import string
import sys
from collections import Counter

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        s = input().strip()
        for i in range(n // 2):
            is_palindrome = s[i] == s[n - 1 - i]
            if i + k >= n:
                is_k_complete = True
            else:
                is_k_complete = s[i] == s[i + k]
            if is_palindrome and is_k_complete:
                continue

            c1 = 0
            for j in range(i + k, n, k):
                if s[i] != s[j]:
                    c1 += 1

            c2 = 0
            for j in range(n - 1 - i, -1, -k):
                if s[i] != s[j]:
                    c2 += 1

            if c1 >= c2:
                for j in range(i + k, n, k):
                    if s[i] != s[j]:

            print(s, i, c1, c2)


if __name__ == '__main__':
    main()
