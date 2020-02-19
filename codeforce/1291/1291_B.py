# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        if n == 1:
            print('Yes')
            continue

        is_break = False
        c = n // 2
        for idx, num in enumerate(arr):
            if c >= idx > num:
                is_break = True
                break
            if c < idx and n - 1 - idx > num:
                is_break = True
                break

        if n % 2 == 0 and is_break:
            is_break = False
            # 0 1 3 2 1 0
            for idx, num in enumerate(arr):
                if c - 1 > idx > num:
                    is_break = True
                    break
                if c - 1 == idx and num < c:
                    is_break = True
                    break
                if c <= idx and n - 1 - idx > num:
                    is_break = True
                    break

        if is_break:
            print('No')
        else:
            print('Yes')


if __name__ == '__main__':
    main()
