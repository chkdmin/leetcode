# -*- coding: utf-8 -*-


class Solution:
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            return [nums, nums[::-1]]

        ret = []
        for idx in range(len(nums)):
            permute = self.permute((nums[idx:] + nums[0:idx])[1:])
            for v in permute:
                ret.append([nums[idx]] + v)

        return ret


if __name__ == '__main__':
    print(Solution().permute([1]))
