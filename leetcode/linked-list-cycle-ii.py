# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return f'ListNode({self.val})'


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = q = head
        while p is not None and q is not None:
            p = p.next
            if q.next is None:
                return
            q = q.next.next
            if p == q:
                break

        if p is None or q is None:
            return

        p = head
        while p != q:
            p = p.next
            q = q.next
        return p


def get_head(nums, pos):
    if not nums:
        return
    head = ListNode(nums[0])
    node = head
    cycle_node = head if pos == 0 else None
    for idx in range(1, len(nums)):
        node.next = ListNode(nums[idx])
        node = node.next
        if idx == pos:
            cycle_node = node
    node.next = cycle_node
    return head


if __name__ == '__main__':
    print(Solution().detectCycle(get_head([3, 2, 0, -4], 1)))
