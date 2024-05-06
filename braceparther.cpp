#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> res_vec;
    vector<string> generateParenthesis(int n) {
        string cur_res = "(";
        
        int balance = 0;
        if (n == 1){
            res_vec.push_back("()");
            return res_vec;
        }
        n = n*2;
        DFS(1, n, cur_res, 1);

        // for (int i=0; i<res_vec.size(); i++) {
        //     cout << res_vec[i] << endl;
        // }
        return res_vec;
    }

    void DFS(int step, int n, string& cur_res, int balance){
        if (step == n){
            if (balance == 0){
                res_vec.push_back(cur_res);
            }
            return;
        }

        if (balance < 0){
            return;
        }

        // ---- (
        cur_res += '(';
        DFS(step + 1, n, cur_res, balance + 1);
        cur_res = cur_res.substr(0, cur_res.size()-1);

        cur_res += ')';
        DFS(step + 1, n, cur_res, balance - 1);
        cur_res = cur_res.substr(0, cur_res.size()-1);

        
        // ---- )

    }
};

int main(){
    Solution sol;
    int n = 3;
    sol.generateParenthesis(n);
    return 0;
}