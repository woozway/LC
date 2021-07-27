// two pointers
// T=O(n)
// S=O(1)

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
  ListNode* getKthFromEnd(ListNode* head, int k) {
    ListNode* fast = head;
    int count = 0;
    while (fast && count < k) {
      fast = fast->next;
      count += 1;
    }
    if (count != k) {
      return nullptr;
    }
    ListNode* slow = head;
    while (fast) {
      slow = slow->next;
      fast = fast->next;
    }
    return slow;
  }
};
