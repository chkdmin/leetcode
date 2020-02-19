# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        is_one = False
        one_cnt = 0
        ret = 0
        for c in input():
            if c == '1' and not is_one:
                is_one = True
            elif c == '1' and is_one:
                ret += one_cnt
                one_cnt = 0
            if c == '0' and is_one:
                one_cnt += 1
        print(ret)


if __name__ == '__main__':
    main()
