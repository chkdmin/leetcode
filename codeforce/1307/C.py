# -*- coding: utf-8 -*-
import string
import sys
from collections import Counter

input = sys.stdin.readline


def main():
    s = input()
    c = Counter()
    for t in s:
        c[t] += 1
    ret = 1
    for v in c.values():
        ret *= v
    print(ret)


if __name__ == '__main__':
    main()
