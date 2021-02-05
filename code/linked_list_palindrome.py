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
        p = collections.deque()
        
        if head is None:
            return True
        
        while True:
            p.append(head.val)
            head = head.next
            if head is None:
                break
                
        if len(p) == 0:
            return True

        while len(p) > 1:
            if p.pop() != p.popleft():
                return False

        return True
