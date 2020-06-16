import sys
from collections import Counter

input = sys.stdin.readline


def main():
    int(input())
    nums = list(map(int, input().split()))

    counter = Counter()
    ret = 0
    for num in nums:
        counter[num] += 1
        ret += (counter[num] - 1)

    for num in nums:
        ret -= (counter[num] - 1)
        print(ret)
        ret += (counter[num] - 1)


if __name__ == '__main__':
    main()
