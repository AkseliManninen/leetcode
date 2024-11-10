# Time complexity: O(n)
# Space complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def get_good_nodes(node, max_val): 
            if node == None:
                return 0

            if node.val >= max_val:
                max_val = node.val
                good_nodes = 1
            else:
                good_nodes = 0

            good_nodes_left = get_good_nodes(node.left, max_val)
            good_nodes_right = get_good_nodes(node.right, max_val)
            return good_nodes + good_nodes_left + good_nodes_right
        
        return get_good_nodes(root, root.val)
            
        