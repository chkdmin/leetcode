# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return f'ListNode({self.val}, {self.next})'


class Solution:
    head = None

    def reverse_list_recursive(self, node: ListNode) -> ListNode:
        if node.next is None:
            self.head = node
            return node
        tail = self.reverse_list_recursive(node.next)
        node.next = None
        tail.next = node
        return node

    def reverse_list_iteratively(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        return prev

    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return
        # self.reverse_list_recursive(head)
        # return self.head
        return self.reverse_list_iteratively(head)


if __name__ == '__main__':
    head = ListNode(1)
    node = head
    for idx in range(2, 7):
        node.next = ListNode(idx)
        node = node.next
    print(head)
    print(Solution().reverseList(head))
