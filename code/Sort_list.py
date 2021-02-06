class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class merge_sorting:

    def merge_two_list(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.merge_two_list(l1.next, l2)
        return l1 or l2

    def partitions(self, head):
        if not (head and head.next):
            return head

        half, slow, fast = None, head, head

        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        l1 = self.partitions(head)
        l2 = self.partitions(slow)

        return self.merge_two_list(l1, l2)


def init_linked_list(array: list):
    if not array:
        return array
    head = ListNode(array[0])
    head.next = init_linked_list(array[1:])

    return head


p = init_linked_list([4,1,2,3])

result = merge_sorting()

p = result.partitions(p)
while p:
    print(p.val)
    p = p.next

