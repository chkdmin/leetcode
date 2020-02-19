# -*- coding: utf-8 -*-
import heapq


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f'TreeNode({self.val}, {self.left}, {self.right})'


class Solution:

    def mergeTreesWithBfs(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        우선순위 큐를 이용하여 해당 순서대로 트리노드를 빼올 수 있도록 함
        만약 두개의 트리에 같은 인덱스의 노드가 없다면 그 인덱스 이후는 탐색하지 않고 그대로 인덱스가 있는 노드를 결과에 붙임
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        root = TreeNode(t1.val + t2.val)
        q1 = [(0, t1)]
        q2 = [(0, t2)]
        r = [root]
        idx = 1
        while q1 and q2 and r:
            n1, v1 = heapq.heappop(q1)
            n2, v2 = heapq.heappop(q2)
            node = r.pop(0)
            if n1 > n2:
                heapq.heappush(q1, (n1, v1))
                node.left = v2.left
                node.right = v2.right
                continue
            elif n2 > n1:
                heapq.heappush(q2, (n2, v2))
                node.left = v1.left
                node.right = v1.right
                continue

            if v1.left and v2.left:
                node.left = TreeNode(v1.left.val + v2.left.val)
                heapq.heappush(q1, (idx, v1.left))
                heapq.heappush(q2, (idx, v2.left))
                r.append(node.left)
                idx += 1
            else:
                node.left = v1.left if v1.left else v2.left

            if v1.right and v2.right:
                node.right = TreeNode(v1.right.val + v2.right.val)
                heapq.heappush(q1, (idx, v1.right))
                heapq.heappush(q2, (idx, v2.right))
                r.append(node.right)
                idx += 1
            else:
                node.right = v1.right if v1.right else v2.right
        return root

    def mergeTreesWithDfs(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """ 재귀
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        node = TreeNode(t1.val + t2.val)
        node.left = self.mergeTreesWithDfs(t1.left, t2.left)
        node.right = self.mergeTreesWithDfs(t1.right, t2.right)
        return node


def print_node_for_level(root):
    q = [root]
    while q:
        node = q.pop(0)
        print(node.val if node else None, end=', ')
        if node is not None:
            q.append(node.left)
            q.append(node.right)


if __name__ == '__main__':
    t1 = TreeNode(-9)
    t1.right = TreeNode(2)
    t1.right.left = TreeNode(1)
    t1.right.right = TreeNode(8)
    t1.right.left.left = TreeNode(-4)
    t1.right.right.left = TreeNode(5)
    t1.right.right.left.left = TreeNode(3)
    t1.right.left.left.left = TreeNode(-6)
    t1.right.left.left.left.left = TreeNode(-7)
    t1.right.left.left.right = TreeNode(0)
    t2 = TreeNode(7251)
    t2.left = TreeNode(3)
    print_node_for_level(Solution().mergeTreesWithBfs(t1, t2))
