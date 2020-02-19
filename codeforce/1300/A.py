# -*- coding: utf-8 -*-
import sys
from collections import Counter

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n = int(input())
        arr = map(int, input().split())
        ret = 0
        hap = 0
        for n in arr:
            if n == 0:
                ret += 1
            hap += n
        hap += ret
        if hap == 0:
            ret += 1
        print(ret)


if __name__ == '__main__':
    main()
