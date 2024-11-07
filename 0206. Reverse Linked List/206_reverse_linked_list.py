# Time complexity: O(n)
# Space complexity: O(n)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head:
            return None

        vals = []
        current = head
        while current:
            vals.append(current.val)
            current = current.next
        
        res = ListNode(vals[-1])
        current = res
        for num in reversed(vals[:-1]):
            current.next = ListNode(num)
            current = current.next
        
        return res
        
        