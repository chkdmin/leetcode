import sys

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        a, b, c = map(int, input().split())
        ret = 0
        if a > 0:
            ret += 1
            a -= 1
        if b > 0:
            ret += 1
            b -= 1
        if c > 0:
            ret += 1
            c -= 1

        if a > 1 and b == 1 and c == 1:
            ret += 2
            a -= 2
            b -= 1
            c -= 1
        if b > 1 and a == 1 and c == 1:
            ret += 2
            b -= 2
            a -= 1
            c -= 1
        if c > 1 and a == 1 and b == 1:
            ret += 2
            c -= 2
            a -= 1
            b -= 1

        if a > 0 and b > 0:
            ret += 1
            a -= 1
            b -= 1
        if a > 0 and c > 0:
            ret += 1
            a -= 1
            c -= 1
        if b > 0 and c > 0:
            ret += 1
            b -= 1
            c -= 1
        if a > 0 and b > 0 and c > 0:
            ret += 1
        print(ret)


if __name__ == '__main__':
    main()
