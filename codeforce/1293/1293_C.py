# -*- coding: utf-8 -*-


def main():
    n, q = map(int, input().split())
    cells = dict()
    bad_nei = 0
    for _ in range(q):
        row, col = map(int, input().split())
        was_forbidden = cells.get((row, col))
        if was_forbidden is None or was_forbidden is False:
            cells[(row, col)] = True
            was_forbidden = True
        elif was_forbidden:
            cells[(row, col)] = False
            was_forbidden = False

        if row == 2:
            r = 1
        else:
            r = 2

        for c in range(col - 1, col + 2):
            if cells.get((r, c)) is True:
                if was_forbidden:
                    bad_nei += 1
                else:
                    bad_nei -= 1

        if bad_nei == 0:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
