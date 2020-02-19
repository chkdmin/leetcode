# -*- coding: utf-8 -*-


class Solution:
    cache = {}

    def is_palindromic(self, s: str):
        if s in self.cache:
            return self.cache[s]

        for idx in range(len(s) // 2):
            if s[idx] != s[len(s) - 1 - idx]:
                self.cache[s] = False
                return False

        self.cache[s] = True
        return True

    def countSubstrings(self, s: str) -> int:
        count = len(s)
        for size in range(2, len(s) + 1):
            for i in range(0, len(s) - size + 1):
                if self.is_palindromic(s[i:i + size]):
                    # print(size, i, s[i:i + size])
                    count += 1
        return count


if __name__ == '__main__':
    print(Solution().countSubstrings('asdf' * 1000))
