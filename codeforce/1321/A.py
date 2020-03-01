import sys

input = sys.stdin.readline


def main():
    n = int(input())
    r = list(map(int, input().split()))
    b = list(map(int, input().split()))
    free = 0
    diff = 0
    for idx in range(n):
        if r[idx] == 1 and b[idx] == 0:
            free += 1
        elif r[idx] == 0 and b[idx] == 1:
            diff += 1

    if free == 0:
        print(-1)
        return

    print((diff // free) + 1)


if __name__ == '__main__':
    main()
