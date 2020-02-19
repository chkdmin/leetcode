# -*- coding: utf-8 -*-


def main():
    n1, n2 = map(int, input().split())
    if n1 > n2:
        print('>')
    elif n1 < n2:
        print('<')
    else:
        print('==')


if __name__ == '__main__':
    main()
