# -*- coding: utf-8 -*-


class Solution:
    def containsDuplicate(self, nums):
        a = {}
        for num in nums:
            if a.get(num) is None:
                a[num] = True
            else:
                return True
        return False


if __name__ == '__main__':
    print(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
