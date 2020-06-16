# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    n = int(input())
    arr = [
        int(input())
        for _ in range(n)
    ]
    idx = 0
    num = 1
    stack = []
    ans = []
    while num <= n:
        if num == arr[idx]:
            idx += 1
            num += 1
            ans.append('+')
            ans.append('-')
        elif stack and stack[-1] == arr[idx]:
            idx += 1
            stack.pop()
            ans.append('-')
        else:
            ans.append('+')
            stack.append(num)
            num += 1
    for _ in range(len(stack)):
        if arr[idx] != stack.pop():
            print('NO')
            return
        ans.append('-')
        idx += 1

    for t in ans:
        print(t)


if __name__ == '__main__':
    main()
