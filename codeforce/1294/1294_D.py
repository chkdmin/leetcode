# -*- coding: utf-8 -*-


def main():
    q, x = map(int, input().split())
    v = [0 for _ in range(x)]
    pair = set((0, i) for i in range(x))
    for _ in range(q):
        n = int(input()) % x
        pair.remove((v[n], n))
        v[n] += 1
        pair.add((v[n], n))
        print(n, pair)
        v1, v2 = tuple(pair)[0]
        print(v1 * x + v2)


if __name__ == '__main__':
    main()
