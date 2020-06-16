# -*- coding: utf-8 -*-
import random
import string
import sys
from collections import Counter

input = sys.stdin.readline
cache = {}


def solve(s):
    if cache.get(s) is not None:
        return cache.get(s)
    ret = len(s)
    for i in range(len(s)):
        if i != 0 and ord(s[i - 1]) - ord(s[i]) == -1:
            ret = min(ret, solve(s[:i] + s[i + 1:]))
        elif i != len(s) - 1 and ord(s[i + 1]) - ord(s[i]) == -1:
            ret = min(ret, solve(s[:i] + s[i + 1:]))
        if cache.get(s[i:]) is not None:
            ret = min(ret, cache.get(s[i:]))
            break
    cache[s] = ret
    return ret


def main():
    n = int(input())
    s = input().strip()
    print(len(s) - solve(s))


if __name__ == '__main__':
    main()
