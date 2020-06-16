import sys

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        ret = 0
        for score in a:
            ret += score
            if ret >= m:
                ret = m
                break
        print(ret)


if __name__ == '__main__':
    main()
