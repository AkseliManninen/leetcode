# Time complexity: O(n)
# Space complexity: O(n) worst case O(log n) best case

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if root == None:
            return 0

        def depth(node, current):
            current += 1
            if node.left and node.right:
                return max(depth(node.left, current), depth(node.right, current))
            elif node.left:
                return depth(node.left, current)
            elif node.right:
                return depth(node.right, current)
            else:
                return current
        
        return depth(root, 0)

        