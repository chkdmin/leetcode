import sys

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        a, b = map(int, input().split())
        a, b = max(a, b), min(a, b)
        if b * 2 >= a:
            print((b * 2) ** 2)
        else:
            print(a ** 2)


if __name__ == '__main__':
    main()
