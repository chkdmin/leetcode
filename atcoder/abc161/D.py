import sys

input = sys.stdin.readline


def get_next_lunlun(num):
    s = 100
    c = v = 1
    while True:
        d = str((num + v) % s)
        a, b = int(d[c]), int(d[c - 1])
        if abs(a - b) <= 1:
            return num + v
        s *= 10
        v *= 10
        c += 1
    return 1


def main():
    k = int(input())
    if k <= 9:
        print(k)
        return
    k -= 9
    ret = 10
    while k > 0:
        ret = get_next_lunlun(ret)
        k -= 1


if __name__ == '__main__':
    main()
