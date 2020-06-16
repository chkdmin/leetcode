import sys

import math

input = sys.stdin.readline


def main():
    h, w = map(int, input().split())
    if h == 1 or w == 1:
        print(1)
        return
    print((math.ceil(w / 2) * math.ceil(h / 2)) + ((w // 2) * (h // 2)))


if __name__ == '__main__':
    main()
