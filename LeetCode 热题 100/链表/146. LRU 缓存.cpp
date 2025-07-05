class Node {
public:
  int k, v;
  Node *pre, *nxt;
  Node(int k=0, int v=0) : k(k), v(v) {}
};

class LRUCache {
private:
  int cap;
  Node *dummy;
  unordered_map<int, Node *> key2node;

  void del(Node *x) {
    x->pre->nxt = x->nxt, x->nxt->pre = x->pre;
  }

  void add(Node *x) { // 头插法
    x->pre = dummy, x->nxt = dummy->nxt, x->pre->nxt = x, x->nxt->pre = x;
  }

  Node *get_node(int key) {
    auto it = key2node.find(key);
    if (it == key2node.end()) return nullptr;
    Node *p = it->second;
    del(p), add(p);
    return p;
  }

public:
  LRUCache(int capacity) {
    cap = capacity, dummy = new Node();
    dummy->pre = dummy, dummy->nxt = dummy;
  }
  
  int get(int key) {
    Node *node = get_node(key);
    return node ? node->v : -1;
  }
  
  void put(int key, int value) {
    Node *node = get_node(key);
    if (node) {
      node->v = value;
      return;
    }

    key2node[key] = node = new Node(key, value);
    add(node);
    if (key2node.size() > cap) {
      Node *back = dummy->pre;
      key2node.erase(back->k);
      del(back);
      delete back;
    }
  }
};