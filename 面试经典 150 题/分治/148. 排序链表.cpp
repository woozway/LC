typedef pair<ListNode *, ListNode *> PLL;

class Solution {    
  ListNode* splitList(ListNode* head, int size) {
    ListNode *t = head;
    for (int i = 0; i < size - 1 && t; i ++ ) t = t->next;
    if (!t || !t->next) return nullptr;
    ListNode *nxt = t->next;
    t->next = nullptr;
    return nxt;
  }

  PLL mergeTwoLists(ListNode *a, ListNode *b) {
    ListNode dummy;
    auto t = &dummy;
    while (a && b) {
      if (a->val <= b->val) t->next = a, a = a->next;
      else t->next = b, b = b->next;
      t = t->next;
    }
    if (a) t->next = a;
    else t->next = b;
    while (t->next) t = t->next;
    
    return {dummy.next, t};
  }

public:
  ListNode* sortList(ListNode* head) {
    int n = 0;
    for (ListNode *t = head; t; t = t->next) n ++ ;

    ListNode dummy(0, head);
    for (int step = 1; step < n; step *= 2) {
      ListNode *ed = &dummy;
      ListNode *t = dummy.next;
      while (t) {
        ListNode *a = t;
        ListNode *b = splitList(a, step);
        t = splitList(b, step);
        auto [head, tail] = mergeTwoLists(a, b);
        ed->next = head;
        ed = tail;
      }
    }
    return dummy.next;
  }
};