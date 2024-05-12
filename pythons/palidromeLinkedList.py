# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head.next is None:
            return True
        slow:ListNode = head
        fast:ListNode = head
        s1:list[int] = []
        # s2:list[int] = []
        
        while (1):
            if fast.next is None:
                break
            elif fast.next.next is None:
                s1.append(slow.val)
                break
            s1.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        while (slow.next is not None):
            if slow.next.val != s1.pop():
                return False
            slow = slow.next
        
        return True