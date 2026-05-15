# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []

        q = deque([(0, root)])

        while q:
            depth, node = q.popleft()

            if depth == len(res):
                res.append(node.val)
            
            if node.right:
                q.append((depth + 1, node.right))
            if node.left:
                q.append((depth + 1, node.left))
        return res
            