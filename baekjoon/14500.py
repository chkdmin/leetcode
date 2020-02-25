# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline

COORDINATES = (
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 0), (1, 0), (2, 0), (3, 0)), # ㅁㅁㅁㅁ

    ((0, 0), (1, 0), (0, 1), (1, 1)), # ㅁㅁ
                                      # ㅁㅁ
    ((0, 0), (0, -1), (0, 1), (1, 0)),
    ((0, 0), (0, -1), (0, 1), (-1, 0)),   # ㅁ
    ((0, 0), (-1, 0), (1, 0), (0, -1)),  # ㅁㅁㅁ
    ((0, 0), (-1, 0), (1, 0), (0, 1)),

    ((0, 0), (-1, 0), (-1, -1), (0, 1)),
    ((0, 0), (-1, 0), (-1, 1), (0, -1)),   # ㅁㅁ
    ((0, 0), (-1, 0), (0, -1), (1, -1)),   # ㅁㅁ
    ((0, 0), (-1, 0), (0, 1), (1, 1)),

    ((0, 0), (0, -1), (1, 0), (2, 0)),
    ((0, 0), (0, 1), (1, 0), (2, 0)),        # ㅁ
    ((0, 0), (0, -1), (-1, 0), (-2, 0)),  # ㅁㅁㅁ
    ((0, 0), (0, 1), (-1, 0), (-2, 0)),
    ((0, 0), (1, 0), (0, -1), (0, -2)),
    ((0, 0), (1, 0), (0, 1), (0, 2)),
    ((0, 0), (-1, 0), (0, -1), (0, -2)),
    ((0, 0), (-1, 0), (0, 1), (0, 2)),
)


def get_maximum_tetromino(arr, i, j):
    maximum = 0
    for coordinate in COORDINATES:
        total = 0
        for y, x in coordinate:
            if i + y >= len(arr):
                total = 0
                break
            elif i + y < 0:
                total = 0
                break
            elif j + x >= len(arr[i + y]):
                total = 0
                break
            elif j + x < 0:
                total = 0
                break
            total += arr[i + y][j + x]
        maximum = max(maximum, total)
    return maximum


def main():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    maximum = 0
    for i in range(n):
        for j in range(m):
            maximum = max(maximum, get_maximum_tetromino(arr, i, j))
    print(maximum)


if __name__ == '__main__':
    main()
