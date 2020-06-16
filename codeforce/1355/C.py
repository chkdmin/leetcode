# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def get_range(n1, n2):
    return range(n1, n2 + 1)


def main():
    a, b, c, d = map(int, input().split())
    rx = get_range(a, b)
    ry = get_range(b, c)
    rz = range(d, c - 1, -1)

    ret = 0
    for x in rx:
        y = b
        while y <= c:
            p = 1
            for z in rz:
                print(x, y, z, ret)
                if x + y <= z:
                    ret += (z - (x + y))
                    p += (z - (x + y))
                    break
                ret += 1
            y += p
    print(ret)


if __name__ == '__main__':
    main()
