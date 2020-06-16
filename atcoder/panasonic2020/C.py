import sys

from math import sqrt

input = sys.stdin.readline


def main():
    a, b, c = map(int, input().split())
    if sqrt(a) + sqrt(b) < sqrt(c):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
