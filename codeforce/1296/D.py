# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    n, a, b, k = map(int, input().split())
    hps = map(int, input().split())
    point = 0
    remain_hps = []
    for hp in hps:
        skip = hp % (a + b)
        if skip == 0:
            skip = a + b
        if skip <= a:
            point += 1
        else:
            remain_hps.append(skip)

    remain_hps.sort()
    uk = 0
    for hp in remain_hps:
        skip = (hp - a) // a
        uk += skip
        if (hp - a) % a != 0 and hp > a:
            uk += 1
        if uk > k:
            break
        point += 1

    print(point)


if __name__ == '__main__':
    main()
