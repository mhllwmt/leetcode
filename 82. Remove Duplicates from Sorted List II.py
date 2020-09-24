class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        new_head = tail = None
        p = head
        while p is not None:
            if p.next is not None and p.next.val == p.val:
                val = p.val
                while p is not None and p.val == val:
                    p = p.next
            else:
                if tail == None:
                    new_head = tail = p
                else:
                    tail.next = p
                    tail = p
                p = p.next
                tail.next = None
        return new_head
