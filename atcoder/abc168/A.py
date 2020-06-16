import sys

input = sys.stdin.readline


def main():
    n = int(input().strip()[-1])
    if n in [2, 4, 5, 7, 9]:
        print('hon')
    elif n in [0, 1, 6, 8]:
        print('pon')
    else:
        print('bon')


if __name__ == '__main__':
    main()
