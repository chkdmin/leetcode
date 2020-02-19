# -*- coding: utf-8 -*-
import sys


def main():
    for _ in range(int(input())):
        print(sum(map(int, sys.stdin.readline().split())))


if __name__ == '__main__':
    main()
