// serilization, tree, preorder
// T=O(n)
// S=O(n)

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:
  void rserialize(TreeNode* root, string& s) {
    if (root == nullptr) {
      s += "None,";
    } else {
      s += to_string(root->val) + ",";
      rserialize(root->left,  s);
      rserialize(root->right, s);
    }
  }

  string serialize(TreeNode* root) {
    string ret;
    rserialize(root, ret);
    return ret;
  }

  TreeNode* rdeserialize(deque<string>& dq) {
    if (dq[0] == "None") {
      dq.pop_front();
      return nullptr;
    }
    TreeNode* root = new TreeNode(stoi(dq.front()));
    dq.pop_front();
    root->left  = rdeserialize(dq);
    root->right = rdeserialize(dq);
    return root;
  }

  TreeNode* deserialize(string data) {
    deque<string> dq;
    string s;
    for (auto& ch : data) {
      if (ch == ',') {
        dq.push_back(s);
        s.clear();
      } else {
        s.push_back(ch);
      }
    }
    return rdeserialize(dq);
  }
};


// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));