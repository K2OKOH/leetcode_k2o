/*
 * @lc app=leetcode.cn id=19 lang=cpp
 *
 * [19] 删除链表的倒数第 N 个结点
 */

# include<iostream>

using namespace std;
struct ListNode 
{
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
    ListNode* removeNthFromEnd(ListNode* head, int n) 
    {
        int cnt = 0;
        int L_len = 0;
        ListNode* temp;
        temp = head;
        cout << head << "," << temp << "\n";
        while(1)
        {
            if(temp->next == nullptr)
            {
                cout << temp->val << "\n";
                L_len = ++cnt;
                cnt = 0;
                break;
            }
            else
            {
                cnt++;
                cout << temp->val << ",";
                temp = temp->next;
            }
        }
        cout << "Len: " << L_len << "\n";
        temp = head;
        while(1)
        {
            cnt++;
            if(L_len-n == 0 && cnt == 1)
            {
                if(L_len == 1)
                {
                    head = nullptr;
                    break;
                }
                head = head->next;
                temp = head;
            }
            else if(cnt == L_len-n)
            {
                temp->next = temp->next->next;
            }
            if(temp->next == nullptr)
            {
                cout << temp->val << "\n";
                break;
            }
            else
            {
                cout << temp->val << ",";
                temp = temp->next;
            }
        }
        cout << head << "," << temp << "\n"; 
        return head;
    }
};
// @lc code=end

