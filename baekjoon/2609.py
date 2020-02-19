# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    a, b = map(int, input().split())
    div = 2
    lcd = 1
    while (div <= a or div <= b) and (a > 1 and b > 1):
        if a % div == 0 and b % div == 0:
            lcd *= div
            a //= div
            b //= div
        else:
            div += 1
    print(lcd)
    print(lcd * a * b)


if __name__ == '__main__':
    main()
