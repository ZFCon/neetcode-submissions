# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(tree1, tree2)->bool:
            if not tree1 and not tree2:
                return True

            if (tree1 and not tree2) or (tree2 and not tree1) or (tree1.val != tree2.val):
                return False

            return dfs(tree1.left, tree2.left) and dfs(tree1.right, tree2.right)


        return dfs(p, q)