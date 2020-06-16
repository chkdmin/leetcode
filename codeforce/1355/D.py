# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    n, s = map(int, input().split())
    if n * 2 > s:
        print('NO')
        return
    print('YES')
    print(f'{"1 " * (n - 1)}{(s - (n - 1))}')
    print(n)


if __name__ == '__main__':
    main()
