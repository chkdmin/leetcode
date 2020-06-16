import sys

input = sys.stdin.readline


def main():
    s = input().strip()
    i = 0
    cnt = 0
    while i <= len(s):
        j = i + 4
        while j <= len(s):
            if int(s[i:j]) % 2019 == 0:
                cnt += 1
                break
            j += 1
        i += 1
    print(cnt)


if __name__ == '__main__':
    main()
