class Solution {
  ListNode* reverseList(ListNode* head) {
    if (!head) return nullptr;
    if (!head->next) return head;
    
    auto res = reverseList(head->next);
    head->next->next = head, head->next = nullptr;
    return res;
  }

public:
  ListNode* reverseKGroup(ListNode* head, int k) {
    // int n = 0;
    // for (ListNode *t = head; t; t = t->next) n ++ ;

    // ListNode dummy(0, head);
    // ListNode *p0 = &dummy, *pre = nullptr, *cur = head;
    // for (; n >= k; n -= k) {
    //   for (int i = 0; i < k; i ++ ) {
    //     ListNode *nxt = cur->next;
    //     cur->next = pre, pre = cur, cur = nxt;
    //   }

    //   ListNode *nxt = p0->next;
    //   p0->next->next = cur, p0->next = pre, p0 = nxt;
    // }
    // return dummy.next;

    // 递归解：找到前k个，反转，后面接递归解的返回值
    ListNode dummy{0, head};
    ListNode *r = &dummy;
    for (int i = 0; r && i < k; i ++ ) r = r->next;
    if (!r) return head;

    ListNode *rest = r->next;
    r->next = nullptr;
    ListNode *p = reverseList(head);
    head->next = reverseKGroup(rest, k);
    return p;
  }
};