# Runtime 0 ms, beats 100%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """

        def get_leafs(node, leafs):
            if node.left:
                get_leafs(node.left, leafs)
            if node.right:
                get_leafs(node.right, leafs)
            if (not node.left) and (not node.right):
                leafs.append(node.val)

        leafs1 = []
        leafs2 = []
        get_leafs(root1, leafs1)
        get_leafs(root2, leafs2)

        return leafs1 == leafs2
