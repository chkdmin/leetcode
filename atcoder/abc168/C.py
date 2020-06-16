import sys

import math

input = sys.stdin.readline


def main():
    a, b, h, m = map(int, input().split())
    c = (30 * h) + ((1 / 2) * m)
    d = 6 * m
    cos = math.cos(abs(c - d))
    ret = (a ** 2) + (b ** 2) - (2 * a * b * cos)
    print(c, d, abs(c - d))
    print(ret ** 0.5)




if __name__ == '__main__':
    main()
