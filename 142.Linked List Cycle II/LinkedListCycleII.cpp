
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
        unordered_set<ListNode *> visited;
        while(head != nullptr)
        {
            // 判断是否读过该点(head是地址)
            if(visited.count(head))
            {
                return head;
            }
            visited.insert(head);
            head = head -> next;
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
        ShowLink(head);
    }
    head->next->next->next->next->next = head->next->next;

    // ShowLink(head);
    head = S.detectCycle(head);
    // ShowLink(head);
    cout << "Out: " << head->val << "\n";
    return 0;
}
