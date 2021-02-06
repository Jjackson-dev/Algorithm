# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import collections


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        rev = None
        
        if head is None:
            return True
        
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            
        if  fast:
            slow = slow.next
        #while slow:
         #   if slow.val != rev.val:
          #      return False
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
