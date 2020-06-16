# -*- coding: utf-8 -*-
import sys
from collections import Counter

from math import sqrt

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        arr = [
            input().strip()
            for _ in range(n)
        ]

        ret = ''
        change_counter = [0 for _ in range(n)]
        for i in range(m):
            c = Counter()
            for j in range(n):
                c[arr[j][i]] += 1

            count = 0
            t = ''
            for k, v in c.items():
                if v > count:
                    is_no = False
                    for j in range(n):
                        if arr[j][i] != k and change_counter[j] > 0:
                            is_no = True
                            break
                    if is_no:
                        continue
                    count = v
                    t = k

            ret += t
            for j in range(n):
                if arr[j][i] != t:
                    change_counter[j] += 1
                    if change_counter[j] > 1:
                        ret = -1

            if ret == -1:
                break

        print(ret)


if __name__ == '__main__':
    main()
