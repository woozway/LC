class Solution {
public:
  ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
    auto &a = list1, &b = list2;

    ListNode dummy; // 设置dummy总有益于链表处理
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
};