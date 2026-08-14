# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = [1]

        # Added max_val to keep track of the highest value seen from the root
        def dfs(node: TreeNode, max_val: int) -> None:
            if not node:
                return
                
            if node.left is not None:
                # Compare the left child to max_val instead of its immediate parent
                counter[0] += 1 if max_val <= node.left.val else 0
                # Pass down the new maximum value for the left path
                dfs(node.left, max(max_val, node.left.val))
            
            if node.right is not None:
                # Compare the right child to max_val instead of its immediate parent
                counter[0] += 1 if max_val <= node.right.val else 0
                # Pass down the new maximum value for the right path
                dfs(node.right, max(max_val, node.right.val))

        # Pass the root's value as the initial max_val
        dfs(root, root.val)
        return counter[0]