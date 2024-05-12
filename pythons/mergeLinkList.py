class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        if list2 is None:
            return list1
        elif list1 is None:
            return list2
        
        dummy1 = ListNode()
        dummy1.next = list1
        dummy2 = ListNode()
        dummy2.next = list2
        
        ptr1 = dummy1
        ptr2 = list2
        
        while (ptr1 is not None and ptr2 is not None):
            if ptr1.next is None:
                ptr1.next = ptr2
                break
            
            if ptr2.val <= ptr1.next.val:
                temp = ptr2
                ptr2 = ptr2.next
                temp.next = ptr1.next
                ptr1.next = temp
                
            ptr1 = ptr1.next
        
        return dummy1.next
        
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        elif head.next is None:
            return head
        
        stack:list[ListNode] = []
        ptr = head
        while ptr:
            stack.append(ptr)
            ptr = ptr.next
        
        newhead = stack.pop()
        prev = newhead
        while stack:
            ptr = stack.pop()
            prev.next = ptr
            prev = prev.next 
        prev.next = None
        return newhead
        pass