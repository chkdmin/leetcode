# -*- coding: utf-8 -*-


class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums) // 3
        nums.sort()
        p, c = nums[0], 0
        r = []
        for num in nums:
            if r and r[0] == num:
                continue
            if p != num:
                c = 0
                p = num
            c += 1
            if c > majority_count:
                r.append(num)
                c = 0
                if len(r) == 2:
                    return r
        return r


if __name__ == '__main__':
    print(Solution().majorityElement([2, 2]))
