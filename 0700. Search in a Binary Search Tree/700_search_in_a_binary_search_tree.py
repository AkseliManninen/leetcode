# Time complexity (worst case): O(n) 
# Memory complexity (worst case): O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """

        def search(node):
            if node is None:
                return None
            if node.val == val:
                return node
            elif val < node.val:
                return search(node.left)
            else:
                return search(node.right)
        
        return search(root)
        