// stack
// T=O(1)
// S=O(n)

class MinStack {
  stack<int> oridinaryStack, minStack;

public:
  /** initialize your data structure here. */
  MinStack() {
    minStack.push(INT_MAX);
  }
  
  void push(int x) {
    oridinaryStack.push(x);
    minStack.push(std::min(minStack.top(), x));
  }
  
  void pop() {
    oridinaryStack.pop();
    minStack.pop();
  }
  
  int top() {
    return oridinaryStack.top();
  }
  
  int min() {
    return minStack.top();
  }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->min();
 */