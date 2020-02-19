# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    _, x = map(int, input().split())
    ret = [
        str(n) for n in map(int, input().split())
        if n < x
    ]
    print(' '.join(ret))


if __name__ == '__main__':
    main()
