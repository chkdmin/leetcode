import math
import sys

input = sys.stdin.readline


def main():
    s = input().strip()
    if len(s) % 2 == 1:
        print('No')
        return

    for idx in range(len(s)):
        if idx % 2 == 0 and s[idx] != 'h':
            print('No')
            return
        elif idx % 2 == 1 and s[idx] != 'i':
            print('No')
            return
    print('Yes')


if __name__ == '__main__':
    main()
