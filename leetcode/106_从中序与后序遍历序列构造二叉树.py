#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 创建一个字典存储中序遍历中值到索引的映射，方便快速查找
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def helper(in_left, in_right):
            # 用于判断构造结构，根据中序遍历确保树的结构唯一
            if in_left > in_right:
                return None

            # 后序遍历的最后一个元素是当前子树的根节点
            val = postorder.pop()
            root = TreeNode(val)

            # 在中序遍历中找到根节点的位置
            index = inorder_map[val]

            # 先构造右子树，因为后序遍历的顺序是左-右-根，而我们是从后往前处理（pop），所以顺序是根-右-左
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)

            return root

        return helper(0, len(inorder) - 1)


# @lc code=end
