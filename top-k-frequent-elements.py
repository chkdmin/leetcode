# -*- coding: utf-8 -*-
import collections
import heapq


class Solution:
    def topKFrequent(self, nums, k: int):
        counter = collections.Counter()
        for num in nums:
            counter[num] += 1
        return list(map(lambda x: x[0], sorted(counter.items(), key=lambda x: x[1], reverse=True)))[:k]


if __name__ == '__main__':
    print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
