# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tail, p = head, head.next
        while p is not None:
            if tail.val != p.val:
                tail.next = p
                tail = p
            p = p.next
        tail.next = None
        return head