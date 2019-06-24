#coding:utf-8
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def buildTree(self, inorder, postorder):
        """

        :param inorder: List[int]
        :param postorder: List[int]
        :return: TreeNode
        """

        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1])
        n = inorder.index(root.val)
        root.left = self.buildTree(inorder[:n], postorder[:n])
        root.right = self.buildTree(inorder[n + 1 :], postorder[n : -1])

        return root


if __name__ == '__main__':
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    print(Solution().buildTree(inorder, postorder).val)
    print(Solution().buildTree(inorder, postorder).left)
    print(Solution().buildTree(inorder, postorder).right)
