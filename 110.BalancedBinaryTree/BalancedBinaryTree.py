import math
import sys
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
                    cur = node_queue.pop()
                    if (cur.left == None):
                        cur.left = n_node
                        break
                    elif (cur.right == None):
                        cur.right = n_node
                        break
                    else:
                        # 如果 cur 不是空结点
                        if (n_node.val != None):
                            node_queue.append(cur.right)
                            node_queue.append(cur.left)
            # 删除空结点
            node_queue = [self.root_node]
            while (len(node_queue) != 0):
                cur = node_queue.pop()
                if  (cur != None):
                    if (cur.val == None):
                        cur = None
                    else:
                        node_queue.append(cur.right)
                        node_queue.append(cur.left)
    
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
    def isBalanced(self, root: TreeNode) -> bool:
        # 若根结点 != -1 -> 是平衡树
        return self.helper(root) != -1

    def helper(self, root: TreeNode):
        if(root == None):
            return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        # 如果子结点非平衡 或 长度不相同
        if (l == -1 or r == -1 or abs(l - r) > 1):
            return -1
        # 返回当前结点长度
        return 1+max(l,r)

if __name__ == '__main__':
    # 初始化数组
    tree_list = [1,2,2,3,3,None,None,4,4]
    root = BinaryTree(tree_list)
    root.DrawTree()

    So = Solution()
    ans = So.isBalanced(root.root_node)
    print(ans)

