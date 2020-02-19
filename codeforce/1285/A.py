# -*- coding: utf-8 -*-
import sys
from collections import Counter

input = sys.stdin.readline


def main():
    _ = int(input())
    counter = Counter()
    commands = input()
    for command in commands:
        counter[command] += 1
    print(counter['L'] + counter['R'] + 1)


if __name__ == '__main__':
    main()
