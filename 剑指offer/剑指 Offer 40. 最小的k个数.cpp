// quick-select
// T=O(n)*, * for mathematical expectation
// S=O(lgn)*

class Solution {
public:
  vector<int> getLeastNumbers(vector<int>& arr, int k) {
    vector<int> v;
    if (arr.size() == 0) {
      return v;
    }
    // might need to use Knuth shuffle algorithm to randomise arr
    int lo = 0, hi = arr.size()-1;
    while (hi > lo) {
      int i = partition(arr, lo, hi);
      if (i < k) lo = i + 1;
      else if (i > k) hi = i - 1;
      else break;
    }
    for (int i = 0; i < k; i++) {
      v.push_back(arr[i]);
    }
    return v;
  }

  int partition(vector<int>& arr, int lo, int hi) {
    int i = lo + 1, j = hi;
    while (i <= j) {
      while (i <= hi && arr[i] <= arr[lo]) i += 1;
      if (i > j) break;
      while (j > lo && arr[j] >= arr[lo]) j -= 1;
      if (i > j) break;
      swap(arr[i], arr[j]);
    }
    swap(arr[lo], arr[j]);
    return j;
  }
};
