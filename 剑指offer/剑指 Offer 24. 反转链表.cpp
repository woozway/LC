// resursion, linkedlist
// T=O(n)
// S=O(n)

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
  ListNode* reverseList(ListNode* head) {
    if (head == nullptr) {
      return head;
    }
    if (head->next == nullptr) {
      return head;
    }
    ListNode* ret = reverseList(head->next);
    head->next->next = head;
    head->next = nullptr;
    return ret;
  }
};
