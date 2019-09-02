# -*- coding: utf-8 -*-


class Solution:
    def reverseString(self, s) -> None:
        for idx in range(len(s) // 2):
            s[idx], s[len(s) - idx - 1] = s[len(s) - idx - 1], s[idx]


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    print(s)
    Solution().reverseString(s)
    print(s)

