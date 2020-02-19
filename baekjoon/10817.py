# -*- coding: utf-8 -*-


def main():
    n1, n2, n3 = map(int, input().split())
    if n1 >= n2 >= n3 or n3 >= n2 >= n1:
        print(n2)
    elif n2 >= n1 >= n3 or n3 >= n1 >= n2:
        print(n1)
    else:
        print(n3)


if __name__ == '__main__':
    main()
