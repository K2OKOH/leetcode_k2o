/*
 * @lc app=leetcode.cn id=455 lang=cpp
 *
 * [455] 分发饼干
 */
# include<vector>
# include<iostream>
# include<algorithm>

using namespace std;
// @lc code=start
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        int cnt = 0, bis = 0;
        sort(s.begin(),s.end());
        sort(g.begin(),g.end());
        for(int i=0;i<g.size();i++)
        {
            for(int j=bis;j<s.size();j++)
            {
                if(g[i]<=s[j])
                {
                    cnt++;
                    bis = j+1;
                    break;
                }
            }
        }
        return cnt;
    }
};
// @lc code=end
int main()
{
    Solution S;
    vector<int> child={1,2,3},cookies={3};
    int ans = 0;
    ans = S.findContentChildren(child,cookies);
    cout << "full child: " << ans << "\n";
    return ans;
}

