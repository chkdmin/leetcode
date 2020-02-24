# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    e, s, m = map(int, input().split())
    re = rs = rm = ret = 0
    while re != e or rs != s or rm != m:
        if re == 15:
            re = 0
        if rs == 28:
            rs = 0
        if rm == 19:
            rm = 0
        re += 1
        rs += 1
        rm += 1
        ret += 1
    print(ret)


if __name__ == '__main__':
    main()
