# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = [root]

        def dfs(tree1: TreeNode, tree2)->bool:
            if not tree1 and not tree2:
                return True
            
            if (tree1 and tree2 and tree1.val != tree2.val) or (tree1 and not tree2) or (tree2 and not tree1):
                return False
            
            return dfs(tree1.left, tree2.left) and dfs(tree1.right, tree2.right)

        while q:
            tree = q.pop()
            if not tree:
                continue
            if tree.val == subRoot.val:
                if dfs(tree, subRoot):
                    return True
            
            q.append(tree.left)
            q.append(tree.right)

        return False