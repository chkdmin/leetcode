import sys

input = sys.stdin.readline


def get_min_max(num):
    min_num = 10
    max_num = 0
    for n in map(int, str(num)):
        if min_num == 0 and max_num == 9:
            break
        if n > max_num:
            max_num = n
        if n < min_num:
            min_num = n
    return min_num, max_num


def main():
    for _ in range(int(input())):
        a, k = input().split()

        ret = int(a)
        for _ in range(1, int(k)):
            min_num, max_num = get_min_max(ret)
            if min_num == 0 or max_num == 0:
                break
            ret += (min_num * max_num)

        print(ret)


if __name__ == '__main__':
    main()
