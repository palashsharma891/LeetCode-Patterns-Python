# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #def reverseUtil(self, curr, prev):
#        if curr.next is None:
 #           self.head = curr
  #          curr.next = prev
   #         return
#        temp = curr.next
 #       curr.next = prev
  #      self.reverseUtil(temp, curr)
    def reverseList(self, head: ListNode) -> ListNode:
#        if head is None or head.next is None:
 #           return head
  #      else:
   #         self.reverseUtil(head, None)
    #        return head
            
        if head is None or head.next is None:
            return head
        else:
            prev = None
            curr = head
            while curr is not None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            head = prev
            return head
