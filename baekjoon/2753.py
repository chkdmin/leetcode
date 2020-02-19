# -*- coding: utf-8 -*-


def main():
    year = int(input())
    if year % 4 != 0:
        print(0)
        return
    if year % 100 == 0 and year % 400 != 0:
        print(0)
        return
    print(1)


if __name__ == '__main__':
    main()
