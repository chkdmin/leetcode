# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline


def main():
    text = list(map(lambda x: x, input().strip()))
    current = len(text)
    for _ in range(int(input())):
        inp = input().split()
        cmd = inp[0]
        if cmd == 'P':
            t = inp[1]
            text.insert(current, t)
            current += 1
        elif cmd == 'L':
            if current > 0:
                current -= 1
        elif cmd == 'D':
            if current < len(text):
                current += 1
        elif cmd == 'B':
            if text and current > 0:
                text.pop(current - 1)
                current -= 1
    print(''.join(text))


if __name__ == '__main__':
    main()
