class Solution {
public:
  ListNode* partition(ListNode* head, int x) {
    if (!head) return nullptr;

    ListNode *t = head;
    vector<ListNode *> a, b;
    while (t) {
      if (t->val < x) a.push_back(t);
      else b.push_back(t);
      t = t->next;
    }

    ListNode dummy(0, head);
    t = &dummy;
    for (int i = 0; i < a.size(); i ++ ) t->next = a[i], t = a[i];
    for (int i = 0; i < b.size(); i ++ ) t->next = b[i], t = b[i];
    t->next = nullptr;
    
    return dummy.next;
  }
};