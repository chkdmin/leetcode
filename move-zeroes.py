# -*- coding: utf-8 -*-
class Solution:
    def moveZeroes(self, nums) -> None:
        zero_idx = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[zero_idx], nums[idx] = nums[idx], nums[zero_idx]
                zero_idx += 1


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    print(nums)
