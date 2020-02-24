# -*- coding: utf-8 -*-
import sys
from math import sqrt

input = sys.stdin.readline


def solve_with_check_is_prime():
    cache = {}

    def is_prime(number):
        if number == 1:
            return False
        c = cache.get(number)
        if c is not None:
            return c

        for m in range(2, int(sqrt(number)) + 1):
            if number % m == 0:
                cache[number] = False
                return False

        cache[number] = True
        return True

    while True:
        n = int(input())
        if n == 0:
            break

        for pn in range(3, n, 2):
            if (n - pn) % 2 == 0:
                continue
            if not is_prime(pn):
                continue
            if not is_prime(n - pn):
                continue
            print(f'{n} = {pn} + {n - pn}')
            break


def solve_with_eratosthenes_sieve():
    sieve = [True for _ in range(1000001)]
    i = 2
    while i * i <= 1000000:
        if not sieve[i]:
            i += 1
            continue

        j = i * i
        while j <= 1000000:
            sieve[j] = False
            j += i

        i += 1

    while True:
        n = int(input())
        if n == 0:
            break

        for pn in range(3, n, 2):
            if (n - pn) % 2 == 0:
                continue
            if not sieve[pn]:
                continue
            if not sieve[n - pn]:
                continue
            print(f'{n} = {pn} + {n - pn}')
            break


if __name__ == '__main__':
    solve_with_check_is_prime()
