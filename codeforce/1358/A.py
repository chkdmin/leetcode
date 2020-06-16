import math
import sys

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        print(math.ceil((n * m) / 2))


if __name__ == '__main__':
    main()
