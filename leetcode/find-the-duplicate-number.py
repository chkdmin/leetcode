# -*- coding: utf-8 -*-


class Solution:
    def findDuplicate(self, nums) -> int:
        p = q = nums[0]
        while True:
            p = nums[p]
            q = nums[nums[q]]
            if p == q:
                break

        p = nums[0]
        while p != q:
            p = nums[p]
            q = nums[q]
        return p


if __name__ == '__main__':
    print(Solution().findDuplicate([2, 5, 9, 6, 3, 4, 8, 9, 7, 1]))
