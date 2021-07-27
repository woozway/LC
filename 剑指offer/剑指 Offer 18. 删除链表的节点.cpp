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
  ListNode* deleteNode(ListNode* head, int val) {
    if (head == nullptr) {
      return head;
    }
    ListNode* puppet = new ListNode(-1, head);
    ListNode* fast = puppet->next, *slow = puppet;
    while (fast && fast->val != val) {
      fast = fast->next;
      slow = slow->next;
    }
    if (fast == nullptr) {
      return puppet->next;
    }
    slow->next = fast->next;
    return puppet->next;
  }
};
