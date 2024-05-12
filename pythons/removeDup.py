class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(val=-200)
        dummy.next = head
        
        left = dummy
        right = head
        
        while(1):
            if right == None:
                left.next = None
                break
                
            if right.val == left.val:    
                right = right.next
            elif right.val != left.val:
                left.next = right
                left = left.next
                right = right.next
            
        
        return dummy.next
        
        pass