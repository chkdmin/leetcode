# -*- coding: utf-8 -*-
import sys
from collections import Counter

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        c = Counter()
        n = int(input())
        es = map(int, input().split())
        for e in es:
            c[e] += 1

        ret = 0
        c = sorted(c.items())
        stay = 0
        for k, v in c:
            ret += (v // k)
            stay += (v % k)
            if stay >= k:
                stay -= k
                ret += 1

        print(ret)


if __name__ == '__main__':
    main()
