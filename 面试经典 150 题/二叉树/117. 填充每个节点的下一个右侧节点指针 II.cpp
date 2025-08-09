class Solution {
public:
  Node* connect(Node* root) {
    Node dummy;
    Node *t = root;
    while (t) {
      dummy.next = nullptr;
      Node *nxt = &dummy; // 下一层的链表
      while (t) { // 遍历当前层的链表
        if (t->left) {
          nxt->next = t->left;
          nxt = t->left;
        }
        if (t->right) {
          nxt->next = t->right;
          nxt = t->right;
        }
        t = t->next;
      }
      t = dummy.next; // 下一层链表的头节点
    }
    return root;
  }
};