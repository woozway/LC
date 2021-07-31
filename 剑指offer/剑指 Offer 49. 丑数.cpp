// heap
// T=O(nlgn)
// S=O(n)

class Solution {
public:
  int nthUglyNumber(int n) {
    priority_queue<long, vector<long>, greater<long>> minHeap;
    minHeap.push(1);
    vector<long> primeFactors {2,3,5};
    unordered_set<long> seen {1};
    for (int i = 0; i < n-1; i++) {
      int topMin = minHeap.top();
      minHeap.pop();
      for (auto& factor : primeFactors) {
        long ugly = factor * topMin;
        if (seen.find(ugly) == seen.end()) {
          minHeap.push(ugly);
          seen.insert(ugly);
        }
      }
    }
    return minHeap.top();
  }
};

