import math
from operator import le
import sys
from tkinter.tix import Tree
from typing import Optional
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

class TreeNode:
    def __init__(self, val=0, left_node=None, right_node=None, index=None) -> None:
        self.val = val
        self.left = left_node
        self.right = right_node
        self.index = index

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
                    cur = node_queue.pop(0)
                    if (cur.left == None):
                        cur.left = n_node
                        break
                    elif (cur.right == None):
                        cur.right = n_node
                        break
                    else:
                        # 如果 cur 不是空结点
                        if (cur.val != None):
                            node_queue.append(cur.left)
                            node_queue.append(cur.right)
            # 删除空结点
            node_queue = [self.root_node]
            while (len(node_queue) != 0):
                cur = node_queue.pop(0)
                if  (cur != None):
                    if (cur.left != None and cur.left.val == None):
                        cur.left = None
                    if (cur.left != None and cur.right.val == None):
                        cur.right = None
                    else:
                        node_queue.append(cur.left)
                        node_queue.append(cur.right)
    
    def node_index(self):
        node_queue = [self.root_node]
        cnt = 1
        while (len(node_queue) != 0):
            cur = node_queue.pop()
            cur.index = cnt
            cnt += 1
            if (cur.right != None):
                node_queue.append(cur.right)
            if (cur.left != None):
                node_queue.append(cur.left)

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
                node_queue.append(cur.right)
                node_queue.append(cur.left)

    def create_graph(self, G, node, pos={}, x=0, y=0, layer=1):
        pos[str(node.index)+':'+str(node.val)] = (x, y)
        if node.left:
            G.add_edge(str(node.index)+':'+str(node.val), str(node.left.index)+':'+str(node.left.val))
            l_x, l_y = x - 1 / 2 ** layer, y - 1
            l_layer = layer + 1
            self.create_graph(G, node.left, x=l_x, y=l_y, pos=pos, layer=l_layer)
        if node.right:
            G.add_edge(str(node.index)+':'+str(node.val), str(node.right.index)+':'+str(node.right.val))
            r_x, r_y = x + 1 / 2 ** layer, y - 1
            r_layer = layer + 1
            self.create_graph(G, node.right, x=r_x, y=r_y, pos=pos, layer=r_layer)
        return (G, pos)

    def DrawTree(self):   # 绘制二叉树
        graph = nx.DiGraph()
        self.node_index()
        graph, pos = self.create_graph(graph, self.root_node)
        fig, ax = plt.subplots(figsize=(8, 10))  # 比例可以根据树的深度适当调节
        nx.draw_networkx(graph, pos, ax=ax, node_size=300)
        plt.show()

# 利用递归处理
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if (root == None):
            return True
        else:
            return self.isSym(root.left, root.right)
    
    def isSym(self, left: TreeNode, right: TreeNode):
        # 两边都是 None => 该结点对称
        if (left == None and right == None):
            return True
        # 仅有一边是 None => 该结点不对称
        elif (left == None or right == None):
            return False
        # 两边都不是 None
        else:
            # 两边值不同 ==> 不对称
            if (left.val != right.val):
                return False
            # 两边值相同 ==> 看子结点
            else:
                return self.isSym(left.left, right.right) and self.isSym(right.left, left.right)

if __name__ == '__main__':
    # 初始化数组
    tree_list = [1,2,2,3,None,None,3]
    root = BinaryTree(tree_list)
    # root.DrawTree()

    So = Solution()
    ans = So.isSymmetric(root.root_node)
    print(ans)

