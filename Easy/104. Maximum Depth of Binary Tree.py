# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.search_tree(root, 1)
        return self.max_depth
        
    def search_tree(self, root, depth):
        if depth > self.max_depth:
            self.max_depth = depth

        if root.left:
            self.search_tree(root.left, depth + 1)
        if root.right:
            self.search_tree(root.right, depth + 1)