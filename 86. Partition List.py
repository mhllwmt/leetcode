# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        def insert(head: ListNode, tail: ListNode, p: ListNode):
            if tail is None:
                head = tail = p
            else:
                tail.next = p
                tail = tail.next
            tail.next = None
            return head, tail

        h1 = tail1 = None
        h2 = tail2 = None
        p = head
        while p is not None:
            tmp = p.next  # import
            if p.val < x:
                h1, tail1 = insert(h1, tail1, p)
            else:
                h2, tail2 = insert(h2, tail2, p)
            p = tmp
        if tail1 is None:
            head = h2
        else:
            tail1.next = h2
            head = h1
        return head