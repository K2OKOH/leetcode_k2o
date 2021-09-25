# include<vector>
# include<iostream>
# include<algorithm>
# include<string>

using namespace std;

class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> ans;
        vector<string> Now_list(n,string(n,'.'));
        vector<bool> shu(n,false), pie(2*n-1,false), na(2*n,false);
        SearchBack(ans, Now_list, 0, shu, pie, na);
        return ans;
    }
private:
    void SearchBack(vector<vector<string>>& ans, vector<string> & Now_list, int idx_y, \
                    vector<bool> shu, vector<bool> pie, vector<bool> na) {
        // append
        if(idx_y == Now_list.size()) {
            ans.push_back(Now_list);
            return;
        }
        // next
        for(int idx_x=0;idx_x<Now_list.size();idx_x++) {
            // find
            if(shu[idx_x] || pie[idx_x+idx_y] || na[idx_x+Now_list.size()-1-idx_y]) continue;
            Now_list[idx_y][idx_x] = 'Q';
            shu[idx_x] = pie[idx_x+idx_y] = na[Now_list.size()-1-idx_y+idx_x] = true;
            // next
            SearchBack(ans, Now_list, idx_y+1, shu, pie, na);
            shu[idx_x] = pie[idx_x+idx_y] = na[Now_list.size()-1-idx_y+idx_x] = false;
            Now_list[idx_y][idx_x] = '.';

        }
    }
};

int main()
{
    Solution So;
    int n = 4;
    vector<vector<string>> ans;
    ans = So.solveNQueens(n);
    for(auto a : ans) {
        for(auto line : a) {
            cout << line << endl;
        }
        cout << endl;
    }
    return 0;
}
