# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: TreeNode) -> None:
            if not node:
                return
            right = node.right
            node.right = node.left
            node.left = right

            dfs(node.right)
            dfs(node.left)
            
        dfs(root)
        return root