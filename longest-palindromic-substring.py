# -*- coding: utf-8 -*-
class Solution:

    def helper(self, s, start, end):
        if end - start <= 1:
            return 1
        print(start, end)
        for i in range(start, end):
            for j in range(end - 1, i, -1):
                print(s[i], s[j])
                if s[i] == s[j]:
                    self.helper(s, i + 1, j)

    def longestPalindrome(self, s: str) -> str:
        for idx in range(len(s)):
            self.helper(s, idx, len(s))


if __name__ == '__main__':
    Solution().longestPalindrome("abcdedcba")
