import sys

import math

input = sys.stdin.readline


def is_good(arr):
    b_cnt = 0
    w_cnt = 0
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if x + 1 < len(arr[y]) and arr[y][x + 1] != arr[y][x]:
                if arr[y][x] == 'W':
                    w_cnt += 1
                else:
                    b_cnt += 1
            elif x - 1 >= 0 and arr[y][x - 1] != arr[y][x]:
                if arr[y][x] == 'W':
                    w_cnt += 1
                else:
                    b_cnt += 1
            elif y + 1 < len(arr) and arr[y + 1][x] != arr[y][x]:
                if arr[y][x] == 'W':
                    w_cnt += 1
                else:
                    b_cnt += 1
            elif y - 1 >= 0 and arr[y - 1][x] != arr[y][x]:
                if arr[y][x] == 'W':
                    w_cnt += 1
                else:
                    b_cnt += 1
    return b_cnt == w_cnt + 1


def dfs(arr):



def main():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        arr = [[None for _ in range(m)] for _ in range(n)]


if __name__ == '__main__':
    main()
