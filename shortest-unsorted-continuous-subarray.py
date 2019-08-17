# -*- coding: utf-8 -*-


class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        if not nums:
            return nums

        start = end = 0
        s_val = 9999
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < prev:
                if s_val > nums[i]:
                    for j in range(i):
                        if nums[j] > nums[i]:
                            start = j
                            s_val = nums[i]
                            break
                end = i
            else:
                prev = nums[i]
        result = end - start
        if result <= 0:
            return 0
        return result + 1


if __name__ == '__main__':
    print(Solution().findUnsortedSubarray([1, 3, 3, 2]))
