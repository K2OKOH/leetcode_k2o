# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:

#         return List

if __name__ == '__main__':
    def Init_List(Lists:list):
        List = ListNode()
        List_temp = List
        length = len(Lists)
        for idx in range(length):
            List_temp.val = Lists[idx]
            List_temp = List_temp.next
        return List


    List = Init_List([1, 4, 5])
    # temperatures = [73,74,75,71,69,72,76,73]
    # So = Solution()
    # ans = So.dailyTemperatures(temperatures)
    # print(ans)
    a = List
    while(a != None):
        print(a.val)
        a = a.next