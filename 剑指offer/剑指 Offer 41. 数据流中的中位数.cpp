// priority_queue or heap
// T=O(lgn)
// S=O(n)

class MedianFinder {
  priority_queue<int> lo;
  priority_queue<int, vector<int>, greater<int>> hi;
  
public:
  MedianFinder() {}
  
  void addNum(int num) {
    lo.push(num);
    int formerHalfMax = lo.top();
    lo.pop();
    hi.push(formerHalfMax);
    int latterHalfMin = hi.top();
    if (lo.size() < hi.size()) {
      lo.push(hi.top());
      hi.pop();
    }
  }
  
  double findMedian() {
    return lo.size() > hi.size() ? 1.0*lo.top() : 0.5*(lo.top() + hi.top());
  }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */