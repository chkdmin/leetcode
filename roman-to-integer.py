# -*- coding: utf-8 -*-
class Solution:

    ROMAN_MAP = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt2(self, s: str) -> int:
        result = 0
        for idx in range(len(s) - 1):
            if self.ROMAN_MAP[s[idx]] >= self.ROMAN_MAP[s[idx + 1]]:
                result += self.ROMAN_MAP[s[idx]]
            else:
                result -= self.ROMAN_MAP[s[idx]]
        result += self.ROMAN_MAP[s[-1]]
        return result

    def romanToInt(self, s: str) -> int:
        idx = 0
        result = 0
        while idx < len(s) - 1:
            v1 = self.ROMAN_MAP[s[idx]]
            v2 = self.ROMAN_MAP[s[idx + 1]]
            if v1 >= v2:
                result += v1
                idx += 1
            else:
                result += (v2 - v1)
                idx += 2
        if idx == len(s) - 1:
            result += self.ROMAN_MAP[s[-1]]
        return result


if __name__ == '__main__':
    for roman in (
        'III', # 3
        'IV', # 4
        'IX', # 9
        'LVIII', # 58
        'MCMXCIV', # 1994
    ):
        print(Solution().romanToInt2(roman))
