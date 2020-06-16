import sys

input = sys.stdin.readline


def main():
    k = int(input())
    s = input().strip()
    if len(s) > k:
        print(s[:k] + '...')
    else:
        print(s)


if __name__ == '__main__':
    main()
