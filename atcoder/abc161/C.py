import sys

input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    n %= k
    if abs(n - k) < n:
        print(abs(n - k))
    else:
        print(n)


if __name__ == '__main__':
    main()
