# -*- coding: utf-8 -*-
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        result = []
        dq = deque()
        for i in range(len(nums)):
            while dq and dq[-1] < i - k + 1:
                dq.pop()
            while dq and nums[dq[0]] < nums[i]:
                dq.popleft()
            dq.appendleft(i)
            if i >= k - 1:
                result.append(nums[dq[-1]])
        return result


if __name__ == '__main__':
    print(Solution().maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))
