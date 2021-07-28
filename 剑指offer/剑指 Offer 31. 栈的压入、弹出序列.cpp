// stack, greedy, simulation
// T=O(n)
// S=O(n)

class Solution {
public:
  bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
    int popIndex = 0;
    stack<int> s;
    for (auto x : pushed) {
      s.push(x);
      while (!s.empty() && popIndex<popped.size() && s.top()==popped[popIndex]) {
        s.pop();
        popIndex++;
      }
    }
    return popIndex == popped.size();
  }
};
