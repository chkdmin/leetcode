# -*- coding: utf-8 -*-


def main():
    h, m = map(int, input().split())
    if m >= 45:
        print(h, m - 45)
        return

    if h == 0:
        h = 23
    else:
        h -= 1

    m = (60 - (45 - m))
    print(h, m)


if __name__ == '__main__':
    main()
