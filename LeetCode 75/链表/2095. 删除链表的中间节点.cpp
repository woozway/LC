class Solution {
public:
  ListNode* deleteMiddle(ListNode* head) {
    if (!head->next) return nullptr;

    ListNode dummy = ListNode(0, head);
    ListNode *slow = &dummy, *fast = dummy.next;
    while (fast && fast->next) {
      slow = slow->next;
      fast = fast->next->next;
    }
    slow->next = slow->next->next;
    return dummy.next;
  }
};