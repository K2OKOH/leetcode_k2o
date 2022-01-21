from logging.config import valid_ident
import math
import sys
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
            # 是完全二叉树 length = 2^deepth - 1
            self.deepth = math.ceil(math.log2(self.length + 1))
            for idx in range(self.length):
                # 创建树中结点
                n_node = TreeNode(val = l[idx])
                # self.add(n_node)
                # 无根结点，成为根结点
                if (self.root_node == None):
                    self.root_node = n_node
                    continue
                node_queue = [self.root_node]
                while (len(node_queue) != 0):
                    cur = node_queue.pop()
                    if (cur.left == None):
                        cur.left = n_node
                    elif (cur.right == None):
                        cur.right = n_node
                    else:
                        # 如果 cur 不是空结点
                        if (n_node.val != None):
                            node_queue.append(cur.left)
                            node_queue.append(cur.right)
            # 删除空结点
            node_queue = [self.root_node]
            while (len(node_queue) != 0):
                cur = node_queue.pop()
                if  (cur != None):
                    if (cur.val == None):
                        cur = None
                    else:
                        node_queue.append(cur.left)
                        node_queue.append(cur.right)

    def add(self, node:TreeNode):
        # 无根结点，成为根结点
        if (self.root_node == None):
            self.root_node = node
        node_queue = [self.root_node]
        while (len(node_queue) != 0):
            cur = node_queue.pop()
            if (cur.left == None):
                cur.left = node
            elif (cur.right == None):
                cur.right = node
            else:
                node_queue.append(cur.left)
                node_queue.append(cur.right)
    
    def DrawTree(self):
        node_queue = [self.root_node]
        cnt = 1
        while (len(node_queue) != 0):
            cur = node_queue.pop()
            cnt += 1
            if (cur != None):
                sys.stdout.write(str(cur.val)+',')
                node_queue.append(cur.left)
                node_queue.append(cur.right)
            if ((math.log2(cnt))%1 == 0):
                sys.stdout.write("\n")
                sys.stdout.flush()

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
    root.DrawTree()

    So = Solution()
    ans = So.maxDepth(root.root_node)
    print(ans)

