##二叉树的前序遍历


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        print(root.val)
        if root.left:
            self.inorderTraversal(root.left)
        if root.right:
            self.inorderTraversal(root.right)