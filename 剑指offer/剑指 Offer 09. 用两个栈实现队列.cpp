// stack, queue
// push: T=O(1); pop: T=O(1) Amortized
// S=O(n)

class CQueue {
  stack<int> si, so;
public:
  CQueue() {}

  void appendTail(int value) {
    si.push(value);
  }

  int deleteHead() {
    if (so.empty() && si.empty()) {
      return -1;
    }
    if (so.empty()) {
      while (!si.empty()) {
        so.push(si.top());
        si.pop();
      }
    }
    int top = so.top();
    so.pop();
    return top;
  }
};

/**
 * Your CQueue object will be instantiated and called as such:
 * CQueue* obj = new CQueue();
 * obj->appendTail(value);
 * int param_2 = obj->deleteHead();
 */