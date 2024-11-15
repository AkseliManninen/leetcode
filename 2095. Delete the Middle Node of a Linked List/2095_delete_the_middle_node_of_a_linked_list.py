# Time complexity: O(n)
# Space complexity O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        previous = None
        current = head
        fast = head

        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                previous = current
                current = current.next
        
        if previous:
            previous.next = current.next
            return head
        else:
            return None

        
        
        
        