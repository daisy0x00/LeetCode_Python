# coding:utf-8

class TreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

class Solution():
    def buildTree(self, preorder, inorder):
        """
        采用层序输出的方法验证生成的二叉树是否正确，
        用先进先出的队列依次保存层序遍历到的结点，
        然后遍历每个结点的左子结点和右子结点
        :param preorder: List[int]
        :param inoeder: List[int]
        :return: TreeNode
        """
        if not preorder or not inorder:
            return None
        # 前序遍历的第一个结点是根节点
        root_data = TreeNode(preorder[0])
        #
        i = inorder.index(root_data)
        # 递归构造左子树和右子树
        left = self.buildTree(preorder[1 : i + 1], inorder[:i])
        right = self.buildTree(preorder[i + 1:], inorder[i + 1:])

        return TreeNode(root_data, left, right)


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    Solution().buildTree(preorder, inorder)
