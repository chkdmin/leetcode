import sys

import math

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        a, b = map(int, input().split())
        if a % b == 0:
            print(0)
        elif b > a:
            print(b - a)
        else:
            print((b * math.ceil(a / b)) - a)


if __name__ == '__main__':
    main()
