# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0

            left = dfs(node.left)+1
            right = dfs(node.right)+1

            result[0] = max(result[0], left+right-2)
            
            return max(left, right)

        dfs(root)
        return result[0]