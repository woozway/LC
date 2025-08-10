class Solution {
  ListNode* mergeTwoLists(ListNode* a, ListNode* b) {
    ListNode dummy;
    auto t = &dummy;
    while (a && b) {
      if (a->val < b->val) t->next = a, a = a->next;
      else t->next = b, b = b->next;
      t = t->next;
    }
    if (a) t->next = a;
    else t->next = b;
    
    return dummy.next;
  }

public:
  ListNode* mergeKLists(vector<ListNode*>& lists) {
    int n = lists.size();
    if (!n) return nullptr;

    auto &a = lists;
    for (int step = 1; step < n; step *= 2)
      for (int i = 0; i + step < n; i += step * 2)
        a[i] = mergeTwoLists(a[i], a[i + step]);
    
    return a[0];
  }
};