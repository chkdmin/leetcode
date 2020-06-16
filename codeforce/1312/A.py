import sys

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        if n % m == 0:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
