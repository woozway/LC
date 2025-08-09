class Solution {
public:
  ListNode* deleteDuplicates(ListNode* head) {
    ListNode dummy(0, head);
    auto t = &dummy;

    while (t->next && t->next->next) {
      int x = t->next->val;
      if (t->next->next->val != x) t = t->next;
      else while (t->next && t->next->val == x) t->next = t->next->next;
    }
    return dummy.next;
  }
};