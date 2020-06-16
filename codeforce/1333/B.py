# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        # ret = {num: [] for num in arr}
        ret = {}
        for i in range(n):
            cnt = 1
            for j in range(i + 1, n):
                gcd_ret = gcd(arr[i], arr[j])
                if gcd_ret != 1:
                    if gcd_ret not in ret:
                        ret[gcd_ret] = [arr[i]]
                    ret[gcd_ret].append(arr[j])
        for k, v in ret.items():
            # for i in range(len(v)):
            #     for j in range(i + 1, len(v)):
            #         if gcd(arr[i], arr[j]) == 1:
            #             arr.pop()
            print(k, v)


if __name__ == '__main__':
    main()
