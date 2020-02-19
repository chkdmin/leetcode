# -*- coding: utf-8 -*-
from math import sqrt


def main():
    for _ in range(int(input())):
        n = int(input())
        d = n
        ret = []
        for i in range(2, int(sqrt(n))):
            if d % i == 0:
                d /= i
                ret.append(i)
            if len(ret) == 2:
                break
        if len(ret) < 2:
            print('NO')
            continue
        a, b = ret
        c = n // (a * b)
        if a == c or b == c or (a * b * c) != n:
            print('NO')
            continue
        print('YES')
        print(a, b, c)


if __name__ == '__main__':
    main()
