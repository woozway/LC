class Solution {
public:
  ListNode* swapPairs(ListNode* head) {
    // ListNode dummy(0, head);
    // ListNode *pre = &dummy, *cur = head;
    // while (cur && cur->next) {
    //   ListNode *nxt = cur->next, *rest = nxt->next;
    //   pre->next = nxt, nxt->next = cur, cur->next = rest;
    //   pre = cur, cur = rest;
    // }
    // return dummy.next;

    if (!head) return nullptr;
    if (!head->next) return head;
    
    ListNode *nxt = head->next->next;
    ListNode *newHead = head->next;
    head->next->next = head;
    head->next = swapPairs(nxt);
    return newHead;
  }
};