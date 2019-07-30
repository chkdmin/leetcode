# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode):
        if not root:
            return

        result = []
        stack = [root]
        node = root
        while stack:
            if node.left is not None:
                stack.append(node.left)
                node.left = None
                node = stack[-1]
                continue
            else:
                node = stack.pop()
                result.append(node.val)
            if node.right is not None:
                stack.append(node.right)
                node.right = None
                node = stack[-1]
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
    print(root)
    print(Solution().inorderTraversal(root))
