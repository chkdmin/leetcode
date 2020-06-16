# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        text = ' '.join(list(map(lambda x: x[::-1], input().split())))
        print(text)


if __name__ == '__main__':
    main()
