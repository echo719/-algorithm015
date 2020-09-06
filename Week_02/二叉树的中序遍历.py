##二叉树的中序遍历


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        if root.left:
            self.inorderTraversal(root.left)
        print(root.val)
        if root.right:
            self.inorderTraversal(root.right)
