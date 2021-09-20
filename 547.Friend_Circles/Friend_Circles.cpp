# include<vector>
# include<iostream>
# include<algorithm>
# include<string>

using namespace std;

class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int num_p = isConnected.size(), FC = 0;
        for(int idx_p1=0;idx_p1<num_p;idx_p1++) {
            for(int idx_p2=idx_p1;idx_p2<num_p;idx_p2++) {
                if(isConnected[idx_p1][idx_p2] == 1) {
                    FindFriends(isConnected, idx_p1, idx_p2);
                    FC++;
                }
            }
        }
        return FC;
    }
private:
    void FindFriends(vector<vector<int>>& isConnected, int p1, int p2) {
        // 把当前关系消除
        isConnected[p1][p2] = 0;
        isConnected[p2][p1] = 0;
        
        // 找到下一个朋友关系
        for(int p=0;p<isConnected.size();p++) {
            if(isConnected[p2][p]) {
                FindFriends(isConnected, p2, p);
            }
        }
    }
};

int main()
{
    Solution So;
    vector<vector<int>> isConnected = { {1,0,0},
                                        {0,1,0},
                                        {0,0,1} };
    int ans = 0;
    ans = So.findCircleNum(isConnected);
    cout << "Out: [" << ans << "]\n";
    return 0;
}
