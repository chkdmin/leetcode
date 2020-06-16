import sys

input = sys.stdin.readline


def main():
    n, m, s = map(int, input().split())
    ans = [-1 for _ in range(n)]
    travel_map = dict()

    for _ in range(m):
        u, v, a, b = map(int, input().split())
        if u not in travel_map:
            travel_map[u] = dict()
        travel_map[u][v] = dict(coin=a, time=b)

    currencies = [
        int(input().split()[1])
        for _ in range(n)
    ]

    print(travel_map)
    print(currencies)


if __name__ == '__main__':
    main()
