# include <iostream>
# include <vector>
# include <map>
# include <set>
# include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> tup_res;
        sort(nums.begin(), nums.end());
        for (int i=0; i<nums.size() - 2; i++){

            for (int j=i+1; j<nums.size() - 1; j++){
                for (int k=j+1; k<nums.size(); k++){
                    if (nums[i] + nums[j] + nums[k] == 0){
                        vector<int> cur_res;
                        cur_res.push_back(nums[i]);
                        cur_res.push_back(nums[j]);
                        cur_res.push_back(nums[k]);
                        tup_res.insert(cur_res);
                    }
                    if (k == nums.size()-1 || nums[k+1] == nums[k]){
                        k += 1;
                    }
                }
                if (j == nums.size()-1 || nums[j+1] == nums[j]){
                    j += 1;
                }
            }
            if (i == nums.size()-1 || nums[i+1] == nums[i]){
                i += 1;
            }
        }
        vector<vector<int>> res_lst(tup_res.begin(), tup_res.end());
        return res_lst;
    }
};

int main(){
    Solution sol;
    vector<int> inp = {-1,0,1,2,-1,-4};
    sol.threeSum(inp);
    return 0;
}