#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (head == nullptr){
            return nullptr;
        }
        else if (head->next == nullptr){
            return head;
        }
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* left = dummy;
        ListNode* right = head->next;
        ListNode* mid;
        ListNode* temp;

        while (true){
            mid = left->next;
            mid->next = right->next;
            left->next = right;
            right->next = mid;

            if (mid->next == nullptr || mid->next->next == nullptr){
                break;
            }

            right = mid->next->next;
            left = mid;
        }
        
        return dummy->next;
    }
};

int main(){
    return 0;
}