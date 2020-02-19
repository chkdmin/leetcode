# -*- coding: utf-8 -*-
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        for num in nums:
            node = TreeNode(num)








if __name__ == '__main__':
    print(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]))
