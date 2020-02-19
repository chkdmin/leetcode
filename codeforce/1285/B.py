# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    global ret
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        n1 = n2 = 0
        flag = False
        for i in range(len(arr)):
            n1 += arr[i]
            n2 += arr[n - 1 - i]
            if n1 <= 0 or n2 <= 0:
                flag = True
        if flag:
            print('NO')
        else:
            print('YES')


if __name__ == '__main__':
    main()