# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        n, p, pre = 0, head, None
        while p:
            pre = p
            p = p.next
            n += 1

        k %= n
        k = n - k
        if k:
            tail, p = pre, head
            for _ in range(k-1):
                p = p.next

            tail.next = head
            head = p.next
            p.next = None
        return head

