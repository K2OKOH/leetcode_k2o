
# include<vector>
# include<iostream>
# include<algorithm>
# include<string>

using namespace std;

class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        if (heights.empty() || heights[0].empty()) return {};
        int W = heights[0].size(), H = heights.size();
        vector<vector<bool>> T_flag(H,vector<bool>(W,true)), D_flag(H,vector<bool>(W,true));
        vector<vector<int>> ans;
        // 对上边，左边进行搜索
        for(int idx_w=0;idx_w<W;idx_w++) {
            dfs(heights,0,idx_w,T_flag);
        }
        for(int idx_h=1;idx_h<H;idx_h++) {
            dfs(heights,idx_h,0,T_flag);
        }
        // 对下边，右边进行搜索
        for(int idx_w=0;idx_w<W;idx_w++) {
            dfs(heights,H-1,idx_w,D_flag);
        }
        for(int idx_h=0;idx_h<H-1;idx_h++) {
            dfs(heights,idx_h,W-1,D_flag);
        }
        for(int idx_w=0;idx_w<W;idx_w++) {
            for(int idx_h=0;idx_h<H;idx_h++) {
                if(D_flag[idx_h][idx_w] == false && T_flag[idx_h][idx_w] == false)
                ans.push_back({idx_h, idx_w});
            }
        }
        return ans;
    }
private:
    void dfs(vector<vector<int>>& heights, int idx_y, int idx_x, vector<vector<bool>>& flag) {
        // 记录当前值
        if(flag[idx_y][idx_x] == false) return;
        flag[idx_y][idx_x] = false;
        // 寻找下一个
        if(idx_y+1<heights.size() && heights[idx_y][idx_x] <= heights[idx_y+1][idx_x] ) {
            dfs(heights, idx_y+1, idx_x, flag);
        }
        if(idx_x+1<heights[0].size() && heights[idx_y][idx_x] <= heights[idx_y][idx_x+1]) {
            dfs(heights, idx_y, idx_x+1, flag);
        }
        if(idx_y>0 && heights[idx_y][idx_x] <= heights[idx_y-1][idx_x]) {
            dfs(heights, idx_y-1, idx_x, flag);
        }
        if(idx_x>0 && heights[idx_y][idx_x] <= heights[idx_y][idx_x-1]) {
            dfs(heights, idx_y, idx_x-1, flag);
        }
    }
};

int main()
{
    Solution So;
    // vector<vector<int>> heights = {{1,2,3},{8,9,4},{7,6,5}};
    vector<vector<int>> heights = {{1,2,2,3,5},{3,2,3,4,4},{2,4,5,3,1},{6,7,1,4,5},{5,1,1,2,4}};
    vector<vector<int>> ans;
    ans = So.pacificAtlantic(heights);
    for(auto p : ans) {
        cout << "[" << p[0] << ", " << p[1] << "], ";
    }
    return 0;
}
