# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        elif head.next is None:
            return head
        
        dummy = ListNode()
        dummy.next = head
        
        ptr = head
        length = 0
        while ptr:
            ptr = ptr.next
            length += 1
        
        k = k % length
        # print(k)
        ptr = head
        if k == 0:
            return head
        
        left = dummy
        right = left
        for _ in range(k):
            right = right.next
            
        while right.next:
            right = right.next
            left = left.next
            
        # print(left.val)
        right.next = dummy.next
        dummy.next = left.next
        left.next = None
        
        return dummy.next
        
        
        pass
    
    
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
k = 2
sol = Solution()
new_head = sol.rotateRight(head, k)
while new_head:
    print(new_head.val, end=" ")
    new_head = new_head.next