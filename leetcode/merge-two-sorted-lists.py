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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        q = []
        while l1 is not None or l2 is not None:
            if l1 is not None:
                heapq.heappush(q, l1.val)
                l1 = l1.next
            if l2 is not None:
                heapq.heappush(q, l2.val)
                l2 = l2.next
        head = ListNode(heapq.heappop(q))
        r = head
        while q:
            head.next = ListNode(heapq.heappop(q))
            head = head.next
        return r


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(5)
    # l2.next = ListNode(3)
    # l2.next.next = ListNode(4)
    print(Solution().mergeTwoLists(l1, l2))
