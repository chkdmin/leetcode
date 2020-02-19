# -*- coding: utf-8 -*-
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode):
        result = []
        stack = deque()
        while stack or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result


if __name__ == '__main__':
    tree = [1, 2, 3, 4, 5, 9, 10, 6, 8, 7, None, 11, 12, None, 13]
    root = TreeNode(tree[0])
    stack = [root]
    for idx in range(1, len(tree), 2):
        node = stack.pop(0)
        if tree[idx] is not None:
            node.left = TreeNode(tree[idx])
            stack.append(node.left)
        if tree[idx+1] is not None:
            node.right = TreeNode(tree[idx+1])
            stack.append(node.right)
    print(Solution().inorderTraversal(root))
