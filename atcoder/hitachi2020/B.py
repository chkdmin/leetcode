import sys

input = sys.stdin.readline


def main():
    a, b, m = map(int, input().split())
    refrigerators = list(map(int, input().split()))
    microwaves = list(map(int, input().split()))
    tickets = [list(map(int, input().split())) for _ in range(m)]

    x_ret = min(refrigerators)
    y_ret = min(microwaves)
    ret = x_ret + y_ret
    for x, y, c in tickets:
        p = refrigerators[x - 1] + microwaves[y - 1] - c
        ret = min(ret, p)
    print(ret)


if __name__ == '__main__':
    main()
