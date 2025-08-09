class Solution {
public:
  int countNodes(TreeNode* root) {
    if (!root) return 0;

    int h = 0; // 根结点位于底0层，完全二叉树最大层数h
    TreeNode* t = root;
    while (t->left) {
      h ++ ;
      t = t->left;
    }
    // 完全二叉树中节点个数为：[2^h - 1 + (1), 2^h - 1 + (2^h)]，
    // 因为最底层有：1~2^h个，所以可以二分查找到底一共有多少个节点
    int l = 1 << h, r = (1 << h + 1) - 1;
    while (l < r) {
      int mid = l + r + 1 >> 1;
      if (exist(root, h, mid)) l = mid;
      else r = mid - 1;
    }
    return l;
  }

  // 在高度为h的完全二叉树中找编号为k的节点（节点编号从1开始）是否存在
  // k的最高位（h位）一定为1，其余各位从高到低对应从root到k节点的路径
  bool exist(TreeNode *root, int h, int k) {
    TreeNode *t = root;
    for (int i = h - 1; ~i; i -- )
      if ((k >> i) & 1) t = t->right;
      else t = t->left;
    return t != nullptr;
  }
};