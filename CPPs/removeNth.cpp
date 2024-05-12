
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(0); // Dummy node
        dummy->next = head;
        ListNode* left = dummy;
        ListNode* right = left;

        if (head->next == nullptr){
            return nullptr;
        }

        for(int i=0; i<n; i++){
            right = right->next;
        }
        
        while (right->next != nullptr){
            left = left->next;
            right = right->next;
        }

        if (n != 1){left->next = left->next->next;}
        else {left->next = nullptr;}
        
        return dummy->next;
    }
};