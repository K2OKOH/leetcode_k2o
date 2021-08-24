
# include<vector>
# include<iostream>
# include<algorithm>

using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) 
    {
        int idx_1=m-1,idx_2=n-1,idx_ans=m+n-1;
        while(idx_2>=0 && idx_1>=0)
        {
            nums1[idx_ans--] = (nums1[idx_1]<=nums2[idx_2])? nums2[idx_2--]:nums1[idx_1--];
        }
        while(idx_2>=0)
        {
            nums1[idx_ans--] = nums2[idx_2--];
        }
    }
};

int main()
{
    Solution S;
    vector<int> nums1={0}, nums2 = {1};
    int m = 0, n = 1;
    S.merge(nums1, m, nums2, n);
    cout << "Out: [";
    for(int i=0;i<m+n;i++)
        cout << nums1[i] << ",";
    cout << "]\n";
    return 0;
}
