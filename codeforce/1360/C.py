# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        even = odd = 0
        is_diff = False
        for i in range(n):
            for j in range(i + 1, n):
                if is_diff:
                    break
                num = abs(arr[i] - arr[j])
                if num == 1:
                    is_diff = True
            if arr[i] % 2 == 0:
                even += 1
            else:
                odd += 1
        even %= 2
        odd %= 2
        if even == 0 and odd == 0:
            print('YES')
        elif even == 1 and odd == 1 and is_diff:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
