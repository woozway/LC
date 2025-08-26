typedef pair<ListNode *, ListNode *> PLL;

class Solution {  
  // 返回从head开始size个节点的后续链表头指针，并把head指向链表截断为size个节点
  ListNode* splitList(ListNode *head, int size) {
    ListNode *t = head;
    for (int i = 0; i < size - 1 && t; i ++ ) t = t->next;
    if (!t || !t->next) return nullptr;
    ListNode *nxt = t->next;
    t->next = nullptr;
    return nxt;
  }

  // 合并两个有序链表，返回合并后的头+尾指针
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

    // O(1)空间，链表的归并排序：按倍增思想分别按1,2,4...为步长合并
    ListNode dummy(0, head);
    for (int step = 1; step < n; step *= 2) {
      ListNode *ed = &dummy;
      ListNode *t = dummy.next;
      while (t) {
        ListNode *a = t;
        ListNode *b = splitList(a, step);
        t = splitList(b, step);
        auto [front, rear] = mergeTwoLists(a, b);
        ed->next = front;
        ed = rear;
      }
    }
    return dummy.next;
  }
};