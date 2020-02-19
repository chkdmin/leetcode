# -*- coding: utf-8 -*-


def main():
    for _ in range(int(input())):
        a, b, c, n = map(int, input().split())
        big = max(a, b, c)
        if a != big:
            n -= (big - a)
        if b != big:
            n -= (big - b)
        if c != big:
            n -= (big - c)
        if n < 0 or n % 3 != 0:
            print('NO')
            continue
        print('YES')


if __name__ == '__main__':
    main()
