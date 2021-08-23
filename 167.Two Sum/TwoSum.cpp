
# include<vector>
# include<iostream>
# include<algorithm>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int num_l = numbers.size();
        int l_idx = 0, r_idx= num_l-1;
        vector<int> ans = {};
        while(l_idx < r_idx)
        {
            if(numbers[l_idx]+numbers[r_idx] == target)
            {
                ans.push_back(l_idx+1);
                ans.push_back(r_idx+1);
                break;
            }
            else if(numbers[l_idx]+numbers[r_idx] < target)
            {
                l_idx++;
            }
            else if(numbers[l_idx]+numbers[r_idx] > target)
            {
                r_idx--;
            }
        }
        return ans;
    }
};

int main()
{
    Solution S;
    vector<int> numbers={2,7,22,15}, ans;
    int target = 9;
    ans = S.twoSum(numbers, target);
    cout << "Out: " << ans[0] << "," << ans[1] << "\n";
    return 0;
}
