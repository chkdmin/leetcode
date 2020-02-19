# -*- coding: utf-8 -*-


def main():
    s = int(input())
    ret = 0
    for i in range(s):
        ret += (1 / (s - i))
    print(ret)


if __name__ == '__main__':
    main()
