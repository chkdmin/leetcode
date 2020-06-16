import sys

input = sys.stdin.readline


def main():
    a, b = map(int, input().split())
    if a <= b:
        print('unsafe')
    else:
        print('safe')


if __name__ == '__main__':
    main()
