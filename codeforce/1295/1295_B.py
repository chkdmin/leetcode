# -*- coding: utf-8 -*-
from collections import Counter


def main():
    for _ in range(int(input())):
        n, x = map(int, input().split())
        s = str(input())
        m = Counter()
        r = []
        for idx in range(n):
            m[s[idx]] += 1
            r.append(m['0'] - m['1'])

        if r[-1] == 0:
            print(-1)
            continue

        if x == 0:
            ret = 1
        else:
            ret = 0
        for num in r:
            if (x - num) / r[-1] >= 0 and (x - num) % r[-1] == 0:
                ret += 1

        print(ret)


if __name__ == '__main__':
    main()
