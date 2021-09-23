# include<vector>
# include<iostream>
# include<algorithm>
# include<string>

using namespace std;

class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> ans;
        vector<int> nums(k,0);
        dfs(nums, ans, 0, 1, n, k);
        return ans;
    }
private:
    void dfs(vector<int> nums, vector<vector<int>>& ans, int layer, int idx, int n, int k) {
        // 终止条件
        if(layer == k) {
            ans.push_back(nums);
            return;
        }
        // 寻找下一个
        for(int i=idx;i<=n;i++) {
            nums[layer] = i;
            layer++;
            dfs(nums, ans, layer, i+1, n, k);
            layer--;
        }
        // return;
    }
};

int main()
{
    Solution So;
    int n = 4, k = 2;
    vector<vector<int>> ans;
    ans = So.combine(n, k);
    for(auto a : ans) {
        cout << "[";
        for(auto num : a) { cout << num << ",";}
        cout << "],";
    }
    return 0;
}
