#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 前序根节点索引，中序遍历的左边界和右边界
        def in_pre_build(root, left, right):
            # 递归终止
            if left > right:
                return
                # 建立根节点
            node = TreeNode(preorder[root])
            # 划分根节点、左子树、右子树
            root_index = ass_dict[preorder[root]]
            # 开启左子树递归
            node.left = in_pre_build(root + 1, left, root_index - 1)
            # 开启右子树递归
            node.right = in_pre_build(root_index - left + root + 1, root_index + 1, right)
            # 回溯返回根节点
            return node

        # 创建一个hash表存储中序列表，加速索引
        ass_dict = {element: i for i, element in enumerate(inorder)}
        return in_pre_build(0, 0, len(inorder) - 1)

    def buildTree(self, preorder, inorder):
        # 创建哈希映射存储中序遍历中值到索引的映射
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        # 使用collections的deque库，可以减少pop第一个元素的时间开销
        preorder = deque(preorder)

        def helper(in_left, in_right):
            if in_left > in_right:
                return None

            # 前序遍历的下一个值就是当前子树的根节点
            root_val = preorder.popleft()
            root = TreeNode(root_val)

            # 在中序遍历中找到根节点的位置
            index = inorder_map[root_val]

            # 先构造左子树，因为前序遍历的顺序是根-左-右
            root.left = helper(in_left, index - 1)
            root.right = helper(index + 1, in_right)

            return root

        return helper(0, len(inorder) - 1)


# @lc code=end
