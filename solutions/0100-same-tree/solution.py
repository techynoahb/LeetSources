# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:

        if p is None and q is None:
            return True
        if q is None and p is not None:
            return False
        if p is None and q is not None:
            return False

        que = deque([p])
        que2 = deque([q])
        while que and que2:
            curr, curr2 = que.popleft(), que2.popleft()
            if curr.val != curr2.val:
                return False
            if curr.left and not curr2.left:
                return False
            if curr.right and not curr2.right:
                return False
            if curr2.left and not curr.left:
                return False
            if curr2.right and not curr.right:
                return False
            if curr2.left and curr.left:
                que.append(curr.left)
                que2.append(curr2.left)
            if curr.right and curr2.right:
                que.append(curr.right)
                que2.append(curr2.right)
        return True
