class Solution {
public:
  ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
    auto &a = list1, &b = list2;

    ListNode dummy{};
    auto cur = &dummy;
    while (a && b) {
      if (a->val < b->val) cur->next = a, a = a->next;
      else cur->next = b, b = b->next;
      cur = cur->next;
    }
    if (a) cur->next = a;
    else cur->next = b;
    
    return dummy.next;
  }
};