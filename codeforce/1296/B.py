# -*- coding: utf-8 -*-


def main():
    for _ in range(int(input())):
        n = int(input())
        ret = n // 10
        while ret != (n + ret) // 10:
            ret = (n + ret) // 10
        print(n + ret)


if __name__ == '__main__':
    main()
