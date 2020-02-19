# -*- coding: utf-8 -*-


def main():
    n1 = int(input())
    n2 = input()
    for idx in range(len(n2) - 1, -1, -1):
        print(n1 * int(n2[idx]))
    print(n1 * int(n2))


if __name__ == '__main__':
    main()
