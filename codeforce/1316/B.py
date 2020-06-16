# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n = int(input())
        s = input().strip()
        ret = s
        ret_idx = 0
        for k in range(1, n):
            if (n - k) % 2 == 0:
                tmp = s[k:] + s[:k]
            else:
                tmp = s[k:] + ''.join(reversed(s[:k]))
            if ret > tmp:
                ret = tmp
                ret_idx = k
        print(ret)
        print(ret_idx + 1)


if __name__ == '__main__':
    main()
