import sys

input = sys.stdin.readline


def solve(n, k):
    if k > n or k == 0:
        return False

    ret = 0
    cnt = 1
    for i in range(k):
        ret += cnt
        cnt += 2
        if ret > n:
            return False

    if n % 2 == 0 and k % 2 == 0:
        return True
    elif n % 2 == 1 and k % 2 == 1:
        return True
    else:
        return False


def main():
    for idx in range(int(input())):
        n, k = map(int, input().split())
        if solve(n, k):
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
