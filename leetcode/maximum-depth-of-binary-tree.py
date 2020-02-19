# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [(1, root)]
        max_depth = 1
        while q:
            depth, node = q.pop()
            if node.left:
                q.append((depth + 1, node.left))
                max_depth = max(max_depth, depth + 1)
            if node.right:
                q.append((depth + 1, node.right))
                max_depth = max(max_depth, depth + 1)
        return max_depth


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(0)
    root.right = TreeNode(0)
    root.left.left = TreeNode(0)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(0)
    print(Solution().maxDepth(root))
