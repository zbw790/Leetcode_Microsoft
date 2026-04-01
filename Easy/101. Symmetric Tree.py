# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #     return self.dfs(root, root)

    # def dfs(self, left_node, right_node):
    #     if not left_node and not right_node:
    #         return True
    #     elif left_node and right_node:
    #         if left_node.val != right_node.val:
    #             return False
    #     else:
    #         return False
        
    #     left = self.dfs(left_node.left, right_node.right)
    #     right = self.dfs(left_node.right, right_node.left)

    #     return (left and right)
        q = []
        q.append(root)
        q.append(root)
        while q:
            t1 = q.pop(0)
            t2 = q.pop(0)

            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None:
                return False
            
            if t1.val != t2.val:
                return False
            
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True


        