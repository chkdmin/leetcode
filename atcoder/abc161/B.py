import sys

input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    limit = sum(arr) / (4 * m)
    cnt = 0
    for num in arr:
        if num >= limit:
            cnt += 1
        if cnt >= m:
            break

    if cnt >= m:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
