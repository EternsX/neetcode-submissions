# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(node):
            if not node:
                return
            
            left = self.maxLength(node.left)
            right = self.maxLength(node.right)
            print(left, right)
            dfs(node.left)
            dfs(node.right)

            self.res = max(self.res, left + right)

        dfs(root)
        return self.res
    
    def maxLength(self, root):
        if not root:
            return 0
        return 1 + max(self.maxLength(root.left), self.maxLength(root.right))