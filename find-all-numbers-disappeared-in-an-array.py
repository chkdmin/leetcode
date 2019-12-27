# -*- coding: utf-8 -*-


class Solution:
    def findDisappearedNumbers(self, nums):
        ret = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = nums[idx] * -1
        for idx, num in enumerate(nums):
            if num > 0:
                ret.append(idx + 1)
        return ret


if __name__ == '__main__':
    print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
