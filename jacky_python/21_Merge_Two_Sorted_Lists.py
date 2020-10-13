from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """ Recursive """
        """ iteration """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        res = dummy = ListNode(-1)
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            
            res = res.next

        if l1 is None:
            res.next = l2
        else:
            res.next = l1
        
        return dummy.next

l1 = [1,2,4]
l2 = [1,3,4]
solution = Solution()
print (solution.mergeTwoLists(l1, l2))