class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dummy = ListNode()
        dummy.next = head
        left:ListNode = dummy
        right:ListNode = dummy.next
        
        if head is None:
            return False
        
        while right.next is not None and right.next.next is not None:
            if left is right:
                return True
            else:
                left = left.next
                right = right.next.next
        return False
        