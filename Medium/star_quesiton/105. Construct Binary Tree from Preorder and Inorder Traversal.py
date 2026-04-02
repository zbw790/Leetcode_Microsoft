# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder 根-左-右
        # inorder 左-根-右
        # 这个交互是穿插的，因为inorder是左中右，我们先进左节点，这个时候如果左边还有树，我们的preorder往前一位就还是左树，一直到没有左
        def array_to_tree(left, right):
            nonlocal preorder_index

            if left > right:
                return None
            
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)

            preorder_index += 1

            root.left = array_to_tree(left, in_order_index_map[root_value] - 1)
            root.right = array_to_tree(in_order_index_map[root_value] + 1, right)

            return root
        
        preorder_index = 0

        in_order_index_map = {}
        for index, value in enumerate(inorder):
            in_order_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)

