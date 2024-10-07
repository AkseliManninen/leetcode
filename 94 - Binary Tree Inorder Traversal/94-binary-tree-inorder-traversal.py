# Runtime 18 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """        
        res = []
        def traverse_inorder(root):
            if root:
                traverse_inorder(root.left)
                res.append(root.val)
                traverse_inorder(root.right)
        
        traverse_inorder(root)

        return res