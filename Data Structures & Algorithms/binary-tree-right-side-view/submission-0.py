# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack = [[root, 0]]
        finder = dict()

        while stack:
            node, index = stack.pop()
            if not node:
                continue
            finder[index] = finder.get(index, [])
            finder[index].append(node.val)
            stack.append([node.left, index+1])
            stack.append([node.right, index+1])

        return [finder[index][0] for index in range(len(finder))]
