# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]
        
        def dfs(node: TreeNode) -> int:
            if not node or not balanced[0]:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            if balanced[0]:
                balanced[0] = -1 <= (left - right) <= 1

            return max(left+1, right+1)

        dfs(root)
        return balanced[0]