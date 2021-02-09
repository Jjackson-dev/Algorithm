class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = None
        prev = None
        while head:
            temp, head.next  = head.next, prev
            prev, head.next = head, temp
            
            head = head.next
        
        return prev
