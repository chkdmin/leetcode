import sys

input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    if m == 0:
        print(10 ** (n - 1))
        return

    numbers = [-1 for _ in range(n)]
    ret = ''
    for _ in range(m):
        s, c = map(int, input().split())
        if s == 1 and c == 0:
            ret = -1

        if numbers[s - 1] == -1:
            numbers[s - 1] = c
        elif numbers[s - 1] != c:
            ret = -1

    if ret == -1:
        print(ret)
        return

    for i in range(len(numbers)):
        if numbers[i] == -1:
            if i == 0:
                numbers[i] = 1
            else:
                numbers[i] = 0
        if numbers[i] < 0 or numbers[i] > 9:
            ret = -1
            break
        ret += str(numbers[i])

    print(int(ret))


if __name__ == '__main__':
    main()
