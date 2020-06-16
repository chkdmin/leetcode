# -*- coding: utf-8 -*-
import random
import string
import sys
from collections import Counter

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n = int(input())
        x = input().strip()
        r1 = r2 = ''
        is_exists = False
        for num in x:
            if is_exists:
                if num == '2':
                    r1 += '0'
                    r2 += '2'
                elif num == '1':
                    r1 += '0'
                    r2 += '1'
                else:
                    r1 += '0'
                    r2 += '0'
            else:
                if num == '2':
                    r1 += '1'
                    r2 += '1'
                elif num == '1':
                    r1 += '1'
                    r2 += '0'
                    is_exists = True
                else:
                    r1 += '0'
                    r2 += '0'
        print(r1)
        print(r2)


if __name__ == '__main__':
    main()
