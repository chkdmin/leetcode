# -*- coding: utf-8 -*-
import random
import string
import sys

import itertools

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        s = input().strip()

        m = {}
        is_break = False
        for idx in range(len(s)):
            if s[idx] not in m:
                m[s[idx]] = set()
            # 이전 확인
            if idx > 0:
                m[s[idx]].add(s[idx - 1])
            # 다음 확인
            if idx < len(s) - 1:
                m[s[idx]].add(s[idx + 1])
            if len(m[s[idx]]) > 2:
                is_break = True
                break

        if is_break:
            print('NO')
            continue

        key = None
        for k, v in m.items():
            if len(v) == 1:
                key = k

        if key is None:
            print('NO')
            continue

        ret = key
        while m[key]:
            next_key = m[key].pop()
            ret += next_key
            m[next_key].remove(key)
            key = next_key

        for c in string.ascii_lowercase:
            if c not in ret:
                ret += c
        print('YES')
        print(ret)


if __name__ == '__main__':
    main()
