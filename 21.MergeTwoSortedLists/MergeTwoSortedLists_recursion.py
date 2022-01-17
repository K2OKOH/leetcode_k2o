from re import S
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
        # 当其中一个列表为空时
        if (list1 == None):
            return list2
        if (list2 == None):
            return list1
        # 取第一个数小的那个数组，后面跟随者的继续比较
        if (list1.val <= list2.val):
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

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