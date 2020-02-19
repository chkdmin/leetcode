# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return f'ListNode({self.val}, {self.next})'


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while True:
            if not node.next:
                return
            node.val = node.next.val
            if node.next.next:
                node = node.next
            else:
                node.next = None
                return


if __name__ == '__main__':
    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)
    print(head)
    Solution().deleteNode(head)
    print(head)
