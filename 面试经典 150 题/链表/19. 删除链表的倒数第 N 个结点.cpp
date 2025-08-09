class Solution {
public:
  ListNode* removeNthFromEnd(ListNode* head, int n) {
    ListNode dummy{0, head};
    ListNode *a = &dummy, *b = &dummy;
    while (n -- ) b = b->next;
    while (b->next) a = a->next, b = b->next;

    ListNode *nxt = a->next;
    a->next = a->next->next;
    delete nxt;
    return dummy.next;
  }
};