
# include<vector>
# include<iostream>
# include<algorithm>

using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) 
    {
        int i=0,j=0,cnt=0;
        while(1)
        {
            if(n<=j)
            {
                break;
            }
            if(cnt>=m)
            {
                for(int a=0;a<n+m-i;a++)
                    nums1.pop_back();
                nums1.insert(nums1.begin()+i,nums2.begin()+j,nums2.end());
                break;
            }
            if(nums2[j]<nums1[i])
            {
                // cout << "i: " << i << ", " << "j: " << j << "\n";
                nums1.pop_back();
                nums1.insert(nums1.begin()+i,nums2[j]);
                i++;
                j++;
            }
            else
            {
                i++;
                cnt++;
            }
        }
    }
};

int main()
{
    Solution S;
    vector<int> nums1={1,2,3,0,0,0}, nums2 = {2,5,6};
    int m = 3, n = 3;
    S.merge(nums1, m, nums2, n);
    cout << "Out: [";
    for(int i=0;i<m+n;i++)
        cout << nums1[i] << ",";
    cout << "]\n";
    return 0;
}
