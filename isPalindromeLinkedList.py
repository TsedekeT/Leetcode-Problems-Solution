# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Find the middle of the linked list using two pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the linked list
        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        
        # Compare the first half with the reversed second half
        while prev:
            if prev.val != head.val:
                return False
            prev, head = prev.next, head.next
        
        return True

