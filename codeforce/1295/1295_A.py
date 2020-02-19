# -*- coding: utf-8 -*-


def main():
    for _ in range(int(input())):
        n = int(input())
        if n % 2 == 1:
            ret = '7' + ('1' * ((n // 2) - 1))
        else:
            ret = '1' * (n // 2)
        print(ret)


if __name__ == '__main__':
    main()
