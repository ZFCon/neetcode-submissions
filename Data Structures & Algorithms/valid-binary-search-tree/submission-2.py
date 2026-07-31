class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode, lowest: float, biggest: float) -> bool:
            if not node:
                return True
            
            # Refactored: A node must be strictly between lowest and biggest
            # If it is outside this range, it's invalid.
            if node.val <= lowest or node.val >= biggest:
                return False
            
            # Refactored: 
            # When going LEFT, the current node.val becomes the new 'biggest' (upper bound).
            # When going RIGHT, the current node.val becomes the new 'lowest' (lower bound).
            return dfs(node.left, lowest, node.val) and dfs(node.right, node.val, biggest)

        # Initialize with -inf as the absolute lowest and +inf as the absolute biggest
        return dfs(root, float("-inf"), float("inf"))