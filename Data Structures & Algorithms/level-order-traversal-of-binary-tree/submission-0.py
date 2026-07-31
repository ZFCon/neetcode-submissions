# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = [[root, 0]]
        result = {}

        while q:
            node, level = q.pop()
            if not node:
                continue
            
            if level not in result:
                result[level] = []
            result[level].append(node.val)
            
            q.extend([[node.right, level+1], [node.left, level+1]])

        formated_result = []
        for i in range(len(result)):
            formated_result.append(result[i])
        return formated_result