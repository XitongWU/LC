#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

class Solution {
public:
    set<vector<int>> res_set;
    // int target;
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> quadruplets;
        sort(nums.begin(), nums.end());
        int n = nums.size();

        for (int i = 0; i < n - 3; ++i) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            for (int j = i + 1; j < n - 2; ++j) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;
                int left = j + 1;
                int right = n - 1;
                while (left < right) {
                    long long total = static_cast<long long>(nums[i]) + nums[j] + nums[left] + nums[right];
                    if (total == target) {
                        quadruplets.push_back({nums[i], nums[j], nums[left], nums[right]});
                        while (left < right && nums[left] == nums[left + 1]) ++left;
                        while (left < right && nums[right] == nums[right - 1]) --right;
                        ++left;
                        --right;
                    } else if (total < target) {
                        ++left;
                    } else {
                        --right;
                    }
                }
            }
        }

        return quadruplets;
    }
};

int main(){
// nums = [1,0,-1,0,-2,2], target = 0
    Solution sol;
    vector<int> nums = {1,0,-1,0,-2,2};
    int target = 0;
    sol.fourSum(nums, target);
}