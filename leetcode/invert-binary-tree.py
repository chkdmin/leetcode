# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f'TreeNode({self.val}, {self.left}, {self.right})'


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        q = [root]
        while q:
            node = q.pop(0)
            if node is None:
                continue
            node.left, node.right = node.right, node.left
            q.append(node.left)
            q.append(node.right)
        return root


def get_root(tree):
    if not tree:
        return
    root = TreeNode(tree.pop(0))
    q = [root]
    while tree:
        node = q.pop(0)
        node.left = TreeNode(tree.pop(0))
        q.append(node.left)
        if tree:
            node.right = TreeNode(tree.pop(0))
            q.append(node.right)
    return root


if __name__ == '__main__':
    root = get_root([4, 2, 7, None, 1, None, 3, 6])
    print(root)
    print(Solution().invertTree(root))
