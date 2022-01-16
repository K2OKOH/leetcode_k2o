# Definition for singly-linked list.
from heapq import heappop, heappush
from typing import List

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
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while (head):
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

if __name__ == '__main__':
    # 初始化数组
    head_list = [1,2,3,4,5]
    list_len = len(head_list)
    head = SingleLinkList(head_list)
   
    So = Solution()
    ans = So.reverseList(head)
    print(ans)

    print('------')
    while(ans != None):
        print(ans.val)
        ans = ans.next
    print('------')