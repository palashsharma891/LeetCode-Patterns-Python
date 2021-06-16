# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        ptr = head
        while ptr != None:
            stack.append(ptr.val)
            ptr = ptr.next
        while head != None:
            if head.val != stack.pop():
                return False
            head = head.next
        return True
