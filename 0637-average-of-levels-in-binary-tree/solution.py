# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        
        res = []
        q = deque([root])

        while q:
            lvl_size = len(q)
            level_sum = 0

            for i in range(lvl_size):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level_sum / lvl_size)
        
            if root is None:
                return []
        
        return res
