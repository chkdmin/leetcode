# -*- coding: utf-8 -*-
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return f'ListNode({self.val}, {self.next})'


class Solution:
    def mergeKLists(self, nodes) -> ListNode:
        q = []
        for node in nodes:
            while node is not None:
                heapq.heappush(q, node.val)
                node = node.next
        head = ListNode(heapq.heappop(q))
        r = head
        while q:
            head.next = ListNode(heapq.heappop(q))
            head = head.next
        return r


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    l3 = ListNode(2)
    l3.next = ListNode(6)
    print(Solution().mergeKLists([l1, l2, l3]))
