import sys

input = sys.stdin.readline


def is_palindrome(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True


def main():
    s = input().strip()
    n = len(s)
    if is_palindrome(s) and is_palindrome(s[0:(n - 1) // 2]) and is_palindrome(s[((n + 3) // 2) - 1:n]):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
