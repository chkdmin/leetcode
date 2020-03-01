# -*- coding: utf-8 -*-
import sys
from bisect import bisect

import math

input = sys.stdin.readline


def main():
    n = int(input())
    b = list(map(int, input().split()))
    max_beauty = 0
    non_visited = [0]
    visited = {}

    while non_visited:
        i = non_visited.pop(0)
        if visited.get(i) is True:
            continue

        visited[i] = True

        beauty = b[i]
        for j in range(i + 1, n):
            if j - i == b[j] - b[i]:
                beauty += b[j]
                visited[j] = True
            elif visited.get(j) is not True:
                non_visited.append(j)
        max_beauty = max(max_beauty, beauty)

    print(max_beauty)


if __name__ == '__main__':
    main()
