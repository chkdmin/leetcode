# -*- coding: utf-8 -*-
import random
import sys

import itertools

input = sys.stdin.readline


def func(arr):
    if len(arr) == 1:
        return arr[0]
    ret = (arr[0] | arr[1]) - arr[1]
    for i in range(2, len(arr)):
        ret = (ret | arr[i]) - arr[i]
    return ret


def main():
    # n = int(input())
    for _ in range(1):
        arr = [6,1,11,8]
        ret = 0
        ret_arr = arr
        for perm_arr in itertools.permutations(arr):
            func_ret = func(perm_arr)
            if func_ret > ret:
                ret = func_ret
                ret_arr = perm_arr
                print(ret, ret_arr)
                # if ret == 4:
                #     print(ret_arr)

        arr.sort(reverse=True)
        if ret != func(arr):
            print(ret_arr, ret, arr, func(arr))
            break
    # print(' '.join(map(str, ret_arr)))


def main2():
    arr = [6, 1, 11, 8]
    big = max(arr)
    counter = [0 for _ in range(len(format(max(arr), 'b')))]
    for n in arr:
        num = format(n, 'b')
        print(n, num)
        for idx in range(len(num) - 1, -1, -1):
            print(idx, num[idx])
            if num[len(num) - idx - 1] == '1':
                counter[idx] += 1
    for n in counter[::-1]:
        if n == 1:
            pass
        print(n)
    print(counter)


def main3():
    n = int(input())
    arr = list(map(int, input().split()))
    big = 0
    ans = -1
    for i in range(len(arr)):
        ret = arr[i]
        for j in range(len(arr)):
            if i == j:
                continue
            ret &= (~arr[j])
        if ret > big:
            big = ret
            ans = i

    print(arr[ans], end=' ')
    for i in range(len(arr)):
        if i == ans:
            continue
        print(arr[i], end=' ')


if __name__ == '__main__':
    main3()
