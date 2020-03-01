import math
import sys

input = sys.stdin.readline


def main():
    bingo = [list(map(int, input().split())) for _ in range(3)]
    for _ in range(int(input())):
        n = int(input())
        for i in range(3):
            for j in range(3):
                if bingo[i][j] == n:
                    bingo[i][j] = True

    ret = False
    for i in range(3):
        is_break = False
        for j in range(3):
            if bingo[i][j] is not True:
                is_break = True
                break
        if not is_break:
            ret = True
            break

    if ret is True:
        print('Yes')
        return

    for i in range(3):
        is_break = False
        for j in range(3):
            if bingo[j][i] is not True:
                is_break = True
                break
        if not is_break:
            ret = True
            break

    if ret is True:
        print('Yes')
        return

    if bingo[0][0] is True and bingo[1][1] is True and bingo[2][2] is True:
        print('Yes')
        return

    if bingo[0][2] is True and bingo[1][1] is True and bingo[2][0] is True:
        print('Yes')
        return

    print('No')


if __name__ == '__main__':
    main()
