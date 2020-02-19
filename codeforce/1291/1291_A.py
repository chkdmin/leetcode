# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        int(input().strip())
        s = [
            n for n in input().strip()
            if int(n) % 2 == 1
        ]
        if len(s) <= 1:
            print(-1)
            continue

        if len(s) % 2 == 0:
            print(''.join(s))
        else:
            print(''.join(s[:-1]))


if __name__ == '__main__':
    main()
