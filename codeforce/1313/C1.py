# -*- coding: utf-8 -*-
import random
import string
import sys
from collections import Counter

input = sys.stdin.readline


def validate(ret, target):
    if not ret:
        return True

    big = ret[0]
    for floors in ret:
        if floors < target and floors < big:
            return False
        big = max(big, floors)
    return True


def get_ret(ret, target):
    # target 을 줄이는 경우
    big_index = 0
    for index, floors in enumerate(ret):
        if floors > ret[big_index]:
            big_index = index

    resize = 10 ** 9 + 1
    for index in range(big_index + 1, len(ret)):
        if resize > ret[index]:
            resize = ret[index]

    small_total = sum(ret) + resize

    # target 을 붙이고 ret 을 줄이는 경우
    small = min(ret)
    big_total = small * len(ret) + target

    # target 을 붙이고 ret 을 줄인다.
    if big_total > small_total:
        ret = [small for _ in range(len(ret))]
        ret.append(target)
        return ret

    # target 을 줄여서 붙인다.
    ret.append(resize)
    return ret


def get_random():
    for _ in range(int(input())):
        n = random.randint(1, 10)
        m = random.sample(range(1, 10), n)
        print(n)
        print(' '.join(map(str, m)))


def main():
    for _ in range(int(input())):
        input()
        m = list(map(int, input().split()))
        ret = []
        for floors in m:
            if validate(ret, floors):
                ret.append(floors)
            else:
                ret = get_ret(ret, floors)
        print(' '.join(map(str, ret)))


if __name__ == '__main__':
    # get_random()
    main()
