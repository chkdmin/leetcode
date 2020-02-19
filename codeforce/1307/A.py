import sys

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        n, d = map(int, input().split())
        arr = list(map(int, input().split()))
        result = arr[0]
        for idx in range(1, len(arr)):
            if idx == 0:
                continue
            if d >= arr[idx] * idx:
                result += arr[idx]
                d -= (arr[idx] * idx)
                continue
            result += (d // idx)
            break
        print(result)


if __name__ == '__main__':
    main()
