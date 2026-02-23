# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        total_sum = 0
        if root.left:
            if root.left.left is None and root.left.right is None:
                total_sum += root.left.val
            else:
                total_sum += self.sumOfLeftLeaves(root.left)        
        total_sum += self.sumOfLeftLeaves(root.right)
        return total_sum