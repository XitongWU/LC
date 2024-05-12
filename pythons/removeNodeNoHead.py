class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node:ListNode) -> None:
        
        left:ListNode = node
        right:ListNode = node.next
        
        while right.next:
            # temp = right.val
            right.val, left.val = left.val, right.val
            right = right.next
            left = left.next
            
        right.val, left.val = left.val, right.val
        left.next = None
        
        pass
        
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        