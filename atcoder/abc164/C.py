import sys

input = sys.stdin.readline


def main():
    d = {}
    for _ in range(int(input())):
        s = input().strip()
        if s in d:
            continue
        d[s] = True
    print(len(d))


if __name__ == '__main__':
    main()
