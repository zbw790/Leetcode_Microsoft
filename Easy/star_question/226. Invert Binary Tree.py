# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 这题只要一直把一个node的左右两个子node交换一下就可以了
        if not root:
            return None

        node_queue = deque([root])

        while node_queue:
            node = node_queue.popleft()
            if node.left:
                node_queue.append(node.left)
            if node.right:
                node_queue.append(node.right)
            
            temp = node.left
            node.left = node.right
            node.right = temp
        
        return root
        