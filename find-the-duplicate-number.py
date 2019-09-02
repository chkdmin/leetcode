# -*- coding: utf-8 -*-


class Solution:
    def findDuplicate(self, nums) -> int:
        p = q = nums[0]
        while True:
            p = nums[p]
            q = nums[nums[q]]
            print(p, q)
            if p == q:
                return p


if __name__ == '__main__':
    print(Solution().findDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]))
