# include<vector>
# include<iostream>
# include<algorithm>
# include<string>
# include<unordered_map>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> num_tab;
        // 统计每个元素的个数
        int max_count = 0;
        for(const int& num : nums) {
            max_count = max(max_count, ++num_tab[num]);
        }
        vector<vector<int>> buckets(max_count + 1);
        for(const auto& p : num_tab) {
            buckets[p.second].push_back(p.first);
        }

        vector<int> ans;
        for(int i=max_count; i>=0&&ans.size()<k; i--) {
            for(const int & num : buckets[i]) {
                ans.push_back(num);
                if(ans.size() == k) {
                    break;
                }
            }
        }
        return ans;
    }
};

int main()
{
    Solution So;
    vector<int> nums = {1,1,1,1,2,2,3,4}, ans;
    int k = 2;
    ans = So.topKFrequent(nums, k);
    cout << "Out: [";
    for(int i=0;i<ans.size();i++) {
        cout << ans[i] << ", ";
    }
    cout << "]" << endl;
    return 0;
}
