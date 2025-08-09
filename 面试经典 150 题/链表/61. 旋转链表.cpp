class Solution {
public:
  ListNode* rotateRight(ListNode* head, int k) {
    if (!k || !head || !head->next) return head;

    int n = 1;
    ListNode *t = head;
    while (t->next) {
      t = t->next;
      n ++ ;
    }
    t->next = head; // 闭合链表，头尾相连

    int m = n - k % n;
    while (m -- ) t = t->next;
  
    ListNode *res = t->next;
    t->next = nullptr;
    return res;
  }
};