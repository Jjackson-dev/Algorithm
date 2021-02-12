# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Swap l1 and l2
        # if l2.val smaller than l1.val
        # elif l1 is None but l2 is not None
        # Do Not swaping when l2 is None
        if not l1 or l2 and l1.val > l2.val:
            l1, l2 = l2, l1 #swap l1 and l2
        
        # l1.next = recursion(l1.next, l2), if l1 is not None 
        # In recursion function, while and if are same 
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        
        #final l1 --> l1:None, l2:None --> Returned from None to 1, in reverse
        return l1
            
             
