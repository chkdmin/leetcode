# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    heights = [int(input()) for _ in range(9)]
    heights.sort()
    total = sum(heights)
    result = []
    for i in range(len(heights)):
        for j in range(i + 1, len(heights)):
            if total - heights[i] - heights[j] == 100:
                result = list(map(str, filter(lambda x: x != heights[i] and x != heights[j], heights)))
                break
        if result:
            break

    print('\n'.join(result))


if __name__ == '__main__':
    main()
