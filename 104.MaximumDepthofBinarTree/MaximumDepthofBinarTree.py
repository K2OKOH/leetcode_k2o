from logging.config import valid_ident
import queue
from turtle import left
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left_node=None, right_node=None) -> None:
        self.val = val
        self.left = left_node
        self.right = right_node

class BinaryTree(object):
    def __init__(self, l, root_node = None) -> None:
        super().__init__()
        self.root_node = root_node
        if (l != []):
            self.length = len(l)
            for idx in range(self.length):
                # 创建树中结点
                n_node = TreeNode(val = l[idx])
                self.add(n_node)
    
    def add(self, node:TreeNode):
        # 无根结点，成为根结点
        if (self.root_node == None):
            self.root_node = node
        node_queue = [self.root_node]
        while (len(node_queue) != 0):
            cur = node_queue.pop()
            if (cur.left_node == None):
                cur.left_node = node
            elif (cur.right_node == None):
                cur.right_node = node
            else:
                node_queue.append(cur.left_node)
                node_queue.append(cur.right_node)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if (root != None):
            return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        else:
            return 0

if __name__ == '__main__':
    # 初始化数组
    tree_list = [3,9,20,None,None,15,7]
    root = BinaryTree(tree_list)

    So = Solution()
    ans = So.maxDepth(root)
    print(ans)

