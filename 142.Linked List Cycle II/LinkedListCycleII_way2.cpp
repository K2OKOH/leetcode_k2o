
# include<vector>
# include<iostream>
# include<algorithm>
# include<unordered_set>

using namespace std;

struct ListNode 
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *detectCycle(ListNode *head)
    {
        struct ListNode *fast, *slow;
        fast = head->next;
        slow = head->next;
        int cnt = 0,meet_flag = 0;
        while(fast != nullptr)
        {
            if(fast == slow)
            {
                cout << "fast: " << fast->val << "\tslow: " << slow->val << "\n";
                if(meet_flag == 0)
                {
                    fast = head->next;
                    slow = slow->next;
                    cnt = 0;
                    meet_flag = 1;
                    continue;
                }
                else
                {
                    return slow;
                }
            }
            fast = fast->next;
            cnt++;
            if(cnt%2 == 0)
            {
                slow = slow->next;
            }
        }
        return nullptr;
    }
};

// 链表中插入node
struct ListNode *AddNode(struct ListNode *head, int i)
{
    // 创建指针的临时空间
    struct ListNode *temp = (struct ListNode*)malloc(sizeof(struct ListNode));
    temp->val = i;
    temp->next = head->next;
    head->next = temp;
    temp = nullptr;
    return head;
}

void ShowLink(struct ListNode *head)
{
    struct ListNode *temp = head->next;
    cout << "ID\tname\n";
    while(temp != nullptr)
    {
        cout << temp->val << " -> ";
        temp = temp -> next;
    }
    cout << "\n";
}

int main()
{
    Solution S;
    int list_l = 4;
    // 先创建一个head node(不放数据?)
    struct ListNode *head = (struct ListNode*)malloc(sizeof(struct ListNode));
    vector<int> nlist = {-4,0,2,3};
    head->next = nullptr;

    for(int i=0;i<4;i++)
    {
        head = AddNode(head, nlist[i]);
        // ShowLink(head);
    }
    head->next->next->next->next->next = head->next->next;

    // ShowLink(head);
    head = S.detectCycle(head);
    // ShowLink(head);
    cout << "Out: " << head->val << "\n";
    return 0;
}
