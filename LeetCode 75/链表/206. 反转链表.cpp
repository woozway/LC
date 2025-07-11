class Solution {
public:
  ListNode* reverseList(ListNode* head) {
    // ListNode *pre = nullptr, *cur = head;
    // while (cur) {
    //   ListNode *nxt = cur->next;
    //   cur->next = pre, pre = cur, cur = nxt;
    // }
    // return pre;
    
    if (!head) return nullptr;
    if (!head->next) return head;
    auto res = reverseList(head->next);
    head->next->next = head, head->next = nullptr;
    return res;
  }
};