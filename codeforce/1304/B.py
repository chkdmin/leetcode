# -*- coding: utf-8 -*-
import sys

import math

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        m = k = 0
        for idx in range(len(arr)):
            if arr[idx] != -1 and k == 0:
                m = 0
                k = arr[idx]

            next = 0
            if idx < len(arr) - 1:
                next = arr[idx + 1] if arr[idx + 1] != -1 else k

            m = max(m, abs(arr[idx] - next))
            # # 맨 앞
            # if idx == 0:
            #     # -1 인 경우
            #     if arr[idx] == -1 and arr[idx + 1] != -1:
            #         m = 0
            #         k = arr[idx + 1]
            # # 맨 뒤
            # elif idx == len(arr) - 1:
            #     pass
            # # 중간
            # else:
            #     # -1 인 경우
            #     if arr[idx] == -1 and arr[idx + 1] != -1:
            #         prev = arr[idx - 1] if arr[idx - 1] != -1 else k
            #         next = arr[idx + 1]
            #         m =
            #         k = (prev + next) // 2



        print(ret)


if __name__ == '__main__':
    main()
