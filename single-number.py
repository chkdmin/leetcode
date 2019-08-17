# -*- coding: utf-8 -*-


class Solution:
    def singleNumberWithDict(self, nums) -> int:
        dic = {}
        for n in nums:
            if n in dic:
                del dic[n]
            else:
                dic[n] = True
        return list(dic.keys())[0]

    def singleNumberWithBit(self, nums) -> int:
        num = 0
        for n in nums:
            num ^= n
        return num
