# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 注意上下界，BST最重要的就是上下界
        return self.dfs(root, float("-inf"), float("inf"))

    def dfs(self, root, low_bound, high_bound):
        if not root:
            return True

        if root.left:
            if root.left.val >= root.val or root.left.val <= low_bound:
                return False
        if root.right:
            if root.right.val <= root.val or root.right.val >= high_bound:
                return False
        
        return self.dfs(root.left, low_bound, root.val) and self.dfs(root.right, root.val, high_bound)