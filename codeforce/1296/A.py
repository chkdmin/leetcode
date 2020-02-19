# -*- coding: utf-8 -*-


def main():
    for _ in range(int(input())):
        c = int(input())
        arr = map(int, input().split())
        odd = 0
        even = 0
        ret = False
        for n in arr:
            if n % 2 == 0:
                even += 1
            else:
                odd += 1
            if odd > 0 and even > 0:
                ret = True
                break

        if ret or (c % 2 == 1 and odd == c):
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
