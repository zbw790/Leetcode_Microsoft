# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        order = []
        self.travel(root, order)
        return order

    def travel(self, root, order):
        if root.left:
            self.travel(root.left, order)
        order.append(root.val)
        if root.right:
            self.travel(root.right, order)
        


