class Solution {
public:
  ListNode* oddEvenList(ListNode* head) {
    if (!head) return nullptr;

    ListNode *evenHd = head->next;
    ListNode *odd = head, *even = head->next;
    while (even && even->next) {
      odd->next = even->next;
      odd = odd->next;
      even->next = odd->next;
      even = even->next;
    }
    odd->next = evenHd;
    return head;
  }
};