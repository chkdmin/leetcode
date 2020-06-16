# -*- coding: utf-8 -*-
import sys
from collections import Counter

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        ret = abs(arr[0] - arr[1])
        for i in range(n):
            for j in range(i + 1, n):
                num = abs(arr[i] - arr[j])
                if ret > num:
                    ret = num
        print(ret)


if __name__ == '__main__':
    main()
