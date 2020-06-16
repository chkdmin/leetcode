import sys

input = sys.stdin.readline


def get_ans(n):
    if n <= 1:
        return 0
    return get_ans(n - 1) + n - 1


def main():
    n, m = map(int, input().split())
    print(get_ans(n) + get_ans(m))


if __name__ == '__main__':
    main()
