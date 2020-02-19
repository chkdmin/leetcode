# -*- coding: utf-8 -*-
import operator


def main():
    for _ in range(int(input())):
        cx = cy = 0
        ret = ''
        packages = []
        for _ in range(int(input())):
            packages.append(tuple(map(int, input().split())))

        is_solved = True
        packages = sorted(packages, key=operator.itemgetter(0, 1))
        for x, y in packages:
            if x > cx:
                ret += ('R' * (x - cx))
                cx = x
            elif x < cx:
                is_solved = False
                break
            if y > cy:
                ret += ('U' * (y - cy))
                cy = y
            elif y < cy:
                is_solved = False
                break
        if not is_solved:
            print('NO')
            continue
        print('YES')
        print(ret)


if __name__ == '__main__':
    main()
