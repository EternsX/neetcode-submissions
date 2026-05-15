# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        memo = {None: 0}
        
        def dfs(node):
            if node in memo:
                return memo[node]
                        
            left = dfs(node.left)
            right = dfs(node.right)

            self.res = max(self.res, left + right)


            output = 1 + max(left, right)
            memo[node] = output
            return output

        dfs(root)
        return self.res