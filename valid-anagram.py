# -*- coding: utf-8 -*-
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cache = Counter()
        for char in s:
            cache[char] += 1
        for char in t:
            cache[char] -= 1
            if cache[char] < 0:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isAnagram('rat', 'car'))
