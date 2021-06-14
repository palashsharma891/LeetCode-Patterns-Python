# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        '''
        curr = head
        l = 0
        while curr.next is not None:
            curr = curr.next
            l += 1
        curr = head
        while l > 0:
            curr = curr.next
            l -= 2
        return curr
        '''
        # two pointers
        slow = fast = head
        while fast and fast.next: #fast and fast.next to avoid None type has no attribute next error
            slow = slow.next
            fast = fast.next.next
        return slow
