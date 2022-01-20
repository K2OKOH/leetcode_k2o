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
    def isPalindrome(self, head: ListNode) -> bool:
        if (head == None or head.next == None):
            return True
        # 找到中点(快慢指针)
        fp = head
        sp = head
        while (fp.next and fp.next.next):
            fp = fp.next.next
            sp = sp.next

        sp = self.reverseList(sp.next)

        # 比较是否相同
        while (sp != None):
            if (head.val != sp.val):
                return False
            head = head.next
            sp = sp.next
        
        return True
    
    # 反转子函数
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        while (head != None):
            next_node = head.next
            head.next = pre
            pre = head
            head = next_node
        return pre




if __name__ == '__main__':
    # 初始化数组
    head = SingleLinkList([1,1,2,1])

    So = Solution()
    ans = So.isPalindrome(head)
    print(ans)

