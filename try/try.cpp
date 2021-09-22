# include<iostream>
# include<vector>
#include <algorithm>

using namespace std;

vector<int> find_p(vector<int> person_i, vector<float> cost_i, vector<float> p_i, int avg_cost) {
    vector<float> ave_p;
    vector<int> ans;
    float cost = 0, person_num = 0;

    for(auto p : person_i) { ave_p.push_back(cost_i[p-1]/p_i[p-1]); }
    sort(person_i.begin(), person_i.end(), [&ave_p](int a,int b){ return ave_p[a-1]<ave_p[b-1]; });
    for(auto p : person_i) {
        cost += cost_i[p-1];
        person_num += p_i[p-1];
        if(cost/person_num < avg_cost)
            ans.push_back(p);
    }
    return ans;
}

int main() {
    vector<int> person_i = {1,2,3,4,5};
    vector<float> cost_i = {2.0,3.0,1.0,4.0,2.0};
    vector<float> p_i = {0.2,0.1,0.2,0.1,0.4};
    float avg_cost = 9.5;
    vector<int> ans;
    ans = find_p(person_i, cost_i, p_i, avg_cost);
    for(auto a : ans) {
        cout << a << ", ";
    }
    cout << endl;
}