#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

class Solution {
public:
    map<char, string> dict_key;
    vector<string> result;


    vector<string> letterCombinations(string digits) {
        dict_key['2'] = "abc";
        dict_key['3'] = "def";
        dict_key['4'] = "ghi";
        dict_key['5'] = "jkl";
        dict_key['6'] = "mno";
        dict_key['7'] = "pqrs";
        dict_key['8'] = "tuv";
        dict_key['9'] = "wxyz";

        //void DFS(int index, string digits, string cur_str);
        if (digits.length() == 0){
            return result;
        }
        DFS(0, digits, "");

        // cout << result[0]<<endl;
        return result;

    }

    void DFS(int index, string digits, string cur_str){
        if (index == digits.length())
        {
            result.push_back(cur_str);
            return;
        }

        for (int i=0; i<dict_key[digits[index]].length(); i++){
            cur_str += dict_key[digits[index]][i];
            // cout << cur_str <<endl;
            DFS(index + 1, digits, cur_str);
            cur_str = cur_str.substr(0, cur_str.length() - 1);
        }

    }
};

int main(){
    Solution sol;
    string input = "";
    vector<string> vec = sol.letterCombinations(input);
    for (size_t i = 0; i < vec.size(); ++i) {
        std::cout << vec[i] << " ";
    }
    return 0;
}




