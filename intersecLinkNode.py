# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ptrA = headA
        ptrB = headB
        
        stackA:list[ListNode] = []
        stackB:list[ListNode] = []
        while (ptrA is not None):
            stackA.append(ptrA)
            ptrA = ptrA.next
        while (ptrB is not None):
            stackB.append(ptrB)
            ptrB = ptrB.next
            
        temp = None
        while(1):
            if len(stackA) == 0 or len(stackB) == 0:
                return temp
            ptrA = stackA.pop()
            ptrB = stackB.pop()
            if ptrA is ptrB:
                temp = ptrA
            else:
                return temp

        
        pass