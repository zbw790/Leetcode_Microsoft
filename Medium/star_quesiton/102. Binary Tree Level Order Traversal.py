# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        final_result = []
        current_list = []
        current_level = 0

        node_queue = deque([(root, 0)])

        while node_queue:
            node, level = node_queue.popleft()

            if level == current_level:
                current_list.append(node.val)
            else:
                current_level += 1
                final_result.append(current_list)
                current_list = []
                current_list.append(node.val)

            if node.left:
                node_queue.append((node.left, level + 1))
            if node.right:
                node_queue.append((node.right, level + 1))     

        final_result.append(current_list)
        return final_result