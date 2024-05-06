// NOT FINISHED

#include <iostream>
#include <string>
#include <cctype>
//#include <typeinfo>
#include <vector>
//#include <map>

using namespace std;

int main()
{
    string test0 = "1werwerw2fas2ad5aaa";
    string test1 = "adj";
    string test2 = "asd3six777fivefiveasd";
    string test4 = "ksjfakhdvsjdvh";

    int get_sum_digit(string str);
    int get_sum_dignum(string str);
    // cout<<test0[3]<<endl;
    // cout<<typeid(test0).name()<<endl;
    
    // cout<<get_sum_digit(test0)<<endl;
    // cout<<get_sum_digit(test1)<<endl;

    // cout<<get_sum_dignum(test2)<<endl;

    cout<< test2.find("four") <<endl;
    cout<< test2.rfind("four") <<endl;
    // cout<<get_sum_dignum(test4)<<endl;

}

int get_sum_digit(string str)
{
    int sum = 0;
    for (int i=0; i < str.length(); i++)
    {
        if (isdigit(str[i]))
        {
            sum += 10 * (str[i] - '0');
            break;
        }
        
        if (i == str.length() - 1)
        {
            return -1;
        }
    }

    for (int j = str.length() - 1; j >= 0; j--)
    {
        if (isdigit(str[j]))
        {
            sum += 1 * (str[j] - '0');
            break;
        }
        
        if (j == 0)
        {
            return -1;
        }
    }

    return sum;
}

int get_sum_dignum(string str)
{
    vector<string> numbers = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    
    int sum = 0;
    int first_dig = 0;

    int index = -1;
    for (int i=0; i < str.length(); i++)
    {
        if (isdigit(str[i]))
        {
            index = i;
            break;
        }
        
        if (i == str.length() - 1)
        {
            index = -1;
            break;
        }
    }

    int min_num = 99999;
    int min_ind = 99999;
    for (int j=0;j<9;j++)
    {
        if (min_num > str.find(numbers[j]))
        {
            min_num = str.find(numbers[j]);
            min_ind = j;
        }
    }

    if (index == -1 && min_ind == 99999)
    {
        return -1;
    }
    else if (index > min_num) 
    { 
        sum += 10 * (min_ind + 1); 
    }
    else
    {
        sum += 10 * (str[index] - '0');
    }
    // -----------
    // cout << sum <<endl;
    index = -1;
    for (int i=str.length() - 1; i >= 0; i--)
    {
        if (isdigit(str[i]))
        {
            index = i;
            break;
        }
        
        if (i == str.length() - 1)
        {
            index = -1;
            break;
        }
    }

    int max_num = -1;
    int max_ind = -1;
    for (int j=0;j<9;j++)
    {
        if (str.rfind(numbers[j]) != string::npos && str.rfind(numbers[j]) > max_num)
        {
            cout << str.rfind(numbers[j]) <<endl;
            max_num = str.rfind(numbers[j]);
            max_ind = j;
        }
    }
    
    cout << max_num <<endl;
    cout << str[index] <<endl;

    if (index < max_num) 
    { 
        sum += 1 * (max_ind + 1); 
    }
    else
    {
        sum += 1 * (str[index] - '0');
    }

    return sum;
}





















