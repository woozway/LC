class Solution {
public:
  int pairSum(ListNode* head) {
    ListNode *t = head;
    vector<ListNode *> a;
    while (t) {
      a.push_back(t);
      t = t->next;
    }

    int res = 0, n = a.size();
    for (int i = 0, j = n - 1; i < j; i ++, j -- )
      res = max(res, a[i]->val + a[j]->val);
    return res;
  }
};