# -*- coding: utf-8 -*-


INT_MAX = 2147483647
INT_MIN = -2147483648


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        negative = 1
        if s[0] == '-' or s[0] == '+':
            negative = int(s[0] + '1')
            s = s[1:]

        try:
            int(s[0])
        except Exception:
            return 0

        n = ''
        for idx, num in enumerate(s):
            try:
                int(num)
            except Exception:
                break
            n += num

        n = int(n) * negative
        if n >= INT_MAX:
            return INT_MAX
        elif n <= INT_MIN:
            return INT_MIN
        return n


if __name__ == '__main__':
    print(Solution().myAtoi('-91283472332'))
