# include<vector>
# include<iostream>
# include<algorithm>
# include<string>
# include<queue>

using namespace std;

class Solution {
public:
    int shortestBridge(vector<vector<int>>& grid) {
        vector<vector<bool>> first(grid.size(),vector<bool>(grid[0].size(),false));
        bool findone = false;
        int ans = 0, level = 0, x, y;
        queue<pair<int,int>> RecordPoint;
        for(int idx_y=0;idx_y<grid.size();idx_y++) {
            for(int idx_x=0;idx_x<grid[0].size();idx_x++) {
                if(grid[idx_y][idx_x] == 1) {
                    dfs(grid, RecordPoint, idx_y, idx_x);
                    findone = true;
                    break;
                }
            }
            if(findone) break;
        }
        // for(auto a : grid) {
        //     for(auto line : a) {
        //         cout << line << ",";
        //     }
        //     cout << endl;
        // }
        // 如果边缘点不为空，进行查找
        while(!RecordPoint.empty()) {
            level++;
            // 根结点个数
            int num_edge = RecordPoint.size();
            while(num_edge--) {
                auto point = RecordPoint.front();
                RecordPoint.pop();
                for(int i=0;i<4;i++) {
                    y = point.first  + dir[i];
                    x = point.second + dir[i+1];
                    if(y>=0 && y<grid.size() && x>=0 && x<grid[0].size()) {
                        if(grid[y][x] == 1) return level;
                        if(grid[y][x] == 2) continue;
                        RecordPoint.push({y,x});
                        grid[y][x] = 2;
                    }
                }
            }
        }
        return 0;
    }
private:
    vector<int> dir = {-1, 0, 1, 0, -1};
    void dfs(vector<vector<int>>& grid, queue<pair<int,int>>& RecordPoint, int idx_y, int idx_x) {
        // kisp
        if(idx_y<0 || idx_y>=grid.size() || idx_x<0 || idx_x>=grid[0].size() \
            || grid[idx_y][idx_x] == 2) {
            return;
        }
        // find
        if(grid[idx_y][idx_x] == 0) {
            RecordPoint.push({idx_y, idx_x});
            return;
        }
        grid[idx_y][idx_x] = 2;
        // next
        for(int fx=0;fx<4;fx++) {
            dfs(grid, RecordPoint, idx_y+dir[fx], idx_x+dir[fx+1]);
        }
    }
};

int main()
{
    Solution So;
    int ans = 0;
    vector<vector<int>> grid = {{1,1,1,1,1},{1,0,0,0,1},{1,0,1,0,1},{1,0,0,0,1},{1,1,1,1,1}};
    ans = So.shortestBridge(grid);
    cout << "length: "<< ans << endl;
    return 0;
}
