# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n = int(input())
        marry = {
            num: False
            for num in range(1, n + 1)
        }
        no_marry_idx = -1
        for idx in range(n):
            arr = list(map(int, input().split()))
            k = arr.pop(0)
            is_marry = False
            for p_idx in arr:
                if marry.get(p_idx) is False:
                    marry[p_idx] = True
                    is_marry = True
                    break

            if not is_marry and no_marry_idx == -1:
                no_marry_idx = idx

        if no_marry_idx == -1:
            print('OPTIMAL')
            continue

        is_break = False
        for k, v in marry.items():
            if not v:
                print('IMPROVE')
                print(no_marry_idx + 1, k)
                is_break = True
                break

        if not is_break:
            print('OPTIMAL')


if __name__ == '__main__':
    main()
