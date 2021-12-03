from typing import List
import random
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self, head: Optional[ListNode]):

        self.head = head

    def getRandom(self) -> int:

        count = 0 
        cur  = self.head # cur为当前节点
        while cur:
            count += 1
            # 等概率取样，每个样本被取到的概率都是1/count
            # 例如，count为1时，概率为1，即res的初值。count为2时，有1/2的几率选中2，如选中，2即为res，替换之前的res，以此类推。
            if random.randint(1,count) == count:
                res = cur.val
            cur = cur.next
        return res

if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    print(l)
    So = Solution(l)
    ans = So.getRandom()
    print(ans)

