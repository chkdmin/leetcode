# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        a = input()
        b = input()
        c = input()
        is_break = False
        for i in range(len(a)):
            if a[i] == b[i] != c[i]:
                is_break = True
                break
            if a[i] != b[i] and a[i] != c[i] and b[i] != c[i]:
                is_break = True
                break

        if is_break:
            print('NO')
        else:
            print('YES')


if __name__ == '__main__':
    main()
