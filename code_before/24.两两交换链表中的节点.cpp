/*
 * @lc app=leetcode.cn id=24 lang=cpp
 *
 * [24] 两两交换链表中的节点
 */
# include<iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) 
    {
        ListNode *temp, *temp1, *temp2, *temp3, *ans, *tp;
        int cnt = 0, list_len = 0;
        temp = head;
        while(temp != nullptr)
        {
            cnt ++;
            temp = temp->next;
        }
        list_len = cnt;
        if(list_len < 2)
            return head;
        // cout << cnt << "\n";
        temp = head;
        ans = head->next;
        tp = head;
        for(int i=0;i<list_len/2;i++)
        {
            // cout << temp->val << ", " << temp->next->val << "\n";
            temp1 = temp;
            temp2 = temp1->next;
            temp3 = temp1->next->next;
            temp = temp2;
            temp->next = temp1;
            temp->next->next = temp3;
            if(i!=0)
                tp->next = temp;
            temp = temp->next->next;
            tp = temp1;
            // cout << temp2->val << ", " << temp1->val << "\n";
        }
        // cout << "ok!";
        return ans;
    }
};
// @lc code=end

