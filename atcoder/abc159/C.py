import sys

input = sys.stdin.readline


def main():
    n = int(input())
    print('%.12f' % (n / 3) ** 3)


if __name__ == '__main__':
    main()
