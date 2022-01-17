from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SingleLinkList(object):
    def __init__(self, l) -> None:
        super().__init__()
        self.val = None
        self.next = None
        # self.header = None
        self.length = 0
        if (l != []):
            self.length = len(l)
            for idx in range(self.length):
                n_node = ListNode(l[idx])
                self.append(n_node)
    
    def is_empty(self):
        if (self.val == None):
            return True
        else:
            return False

    def add(self, node:ListNode):
        if (self.is_empty()):
            self.val = node.val
            self.next = node.next
        else:
            node.next = self.next
            self.next = node
        self.length += 1

    def append(self, node:ListNode):
        current_Node = self
        if (self.is_empty()):
            self.add(node)
        else:
            # 当下一个不为「空」时，持续寻求下一个
            while(current_Node.next != None):
                current_Node = current_Node.next
            # 为「空」的指针指向下一个节点
            current_Node.next = node
            self.length += 1

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(0)
        start = node
        while (list1 and list2):
            if (list1.val > list2.val):
                # 把 list2 结点放入结果列表
                node.next = list2
                # list2 去除头部结点
                list2 = list2.next
            else:
                node.next = list1
                list1 = list1.next
            # 指向下一个结点
            node = node.next
        # 放入剩余结点
        node.next = list1 if list1 else list2
        # 返回头结点
        return start.next

if __name__ == '__main__':
    # 初始化数组
    l1 = [1,2,4]
    l2 = [1,3,4]
    l1 = SingleLinkList(l1)
    l2 = SingleLinkList(l2)
   
    So = Solution()
    ans = So.mergeTwoLists(l1, l2)
    print(ans)

    print('------')
    while(ans != None):
        print(ans.val)
        ans = ans.next
    print('------')