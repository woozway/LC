class MedianFinder {
  priority_queue<int> l; // 左边最大堆
  priority_queue<int, vector<int>, greater<int>> r; // 右边最小堆

public:
  MedianFinder() {
    
  }

  void addNum(int num) {
    if (l.size() == r.size()) {
      r.push(num);
      l.push(r.top());
      r.pop();
    }
    else {
      l.push(num);
      r.push(l.top());
      l.pop();
    }
  }

  double findMedian() {
    if (l.size() > r.size()) return l.top();
    return (l.top() + r.top()) / 2.0;
  }
};