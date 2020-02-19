# -*- coding: utf-8 -*-
from collections import Counter


class Solution:
    def majorityElement(self, nums) -> int:
        majority_count = len(nums) // 2
        m = Counter()
        for num in nums:
            m[num] += 1
            if m[num] > majority_count:
                return num


if __name__ == '__main__':
    print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
