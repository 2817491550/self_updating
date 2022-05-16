# -*- coding: utf-8 -*-
import collections

MAX_VALUE = 65535

class BinaryTreeNode(object):
    def __init__(self, var, left = None, right = None):
        self.var = var
        self.left = left
        self.right = right

class BinaryTreeAction(object):
    def get_min_depth(self, root):
        """获取最小深度
        """
        if not root:
            return 0
        return self.get_min(root)

    def get_min(self, root):
        if not root:
            return MAX_VALUE
        if not root.left and not root.right:
            return 1
        return min(self.get_min(root.left), self.get_min(root.right)) + 1

    def num_of_tree_nodes(self, root):
        """获取树节点个数
        """
        if not root:
            return 0
        return self.num_of_tree_nodes(root.left) + self.num_of_tree_nodes(root.right) + 1

    def num_of_leaf_nodes(self, root):
        """获取叶子节点个数
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return self.num_of_leaf_nodes(root.left) + self.num_of_leaf_nodes(root.right)

    def num_of_k_level_nodes(self, root, k):
        """获取第k层的节点数
        """
        if not root or k < 1:
            return 0
        if k == 1:
            return 1
        return self.num_of_k_level_nodes(root.left, k-1) + self.num_of_k_level_nodes(root.right, k-1)

    def is_balanced(self, root):
        """判断是否为平衡二叉树
        """
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return helper(root) != -1
    
    def is_completed(self, root):
        """是否为完全二叉树
        """
        if not root:
            return False
        queue  = collections.deque()
        # TODO
        pass

    def is_same_tree(self, root1, root2):
        """两棵树是否为同一棵
        """
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.is_same_tree(root1.left, root2.left) and self.is_same_tree(root1.right, root2.right)

    def is_mirror(self, root1, root2):
        """两棵树是否互为镜像
        """
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.is_mirror(root1.left, root2.right) and self.is_mirror(root1.right, root2.left)

    
    
        