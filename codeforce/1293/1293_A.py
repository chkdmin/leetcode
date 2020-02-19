# -*- coding: utf-8 -*-


def main():
    for _ in range(int(input())):
        n, s, k = map(int, input().split())
        m = dict.fromkeys(map(int, input().split()), True)
        stair_count = 0
        s1 = s2 = s
        while True:
            if s1 <= n and not m.get(s1):
                print(stair_count)
                break
            elif s2 > 0 and not m.get(s2):
                print(stair_count)
                break
            stair_count += 1
            s1 += 1
            s2 -= 1


if __name__ == '__main__':
    main()
