import sys

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.sort()
        b.sort()
        for i in range(n):
            print(a[i], end=' ')
        print('')
        for i in range(n):
            print(b[i], end=' ')
        print('')


if __name__ == '__main__':
    main()
