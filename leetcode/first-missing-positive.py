# -*- coding: utf-8 -*-


class Solution:
    def firstMissingPositive(self, nums) -> int:
        r = 1
        c = {}
        for num in nums:
            if num < 0:
                continue
            c[num] = True
            if num == r:
                while True:
                    r += 1
                    if c.get(r) is None:
                        break
        return r


if __name__ == '__main__':
    print(Solution().firstMissingPositive([3, 4, -1, 1]))
