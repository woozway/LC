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
    // need to run Knuth shuffle algorithm to randomise arr first
    int lo = 0, hi = arr.size()-1;
    while (lo < hi) {
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

  int median3(vector<int>& arr, int l, int r) {
    int centre = (l+r)/2;
    if (arr[l] > arr[centre]) swap(arr[l], arr[centre]);
    if (arr[l] > arr[r]) swap(arr[l], arr[r]);
    if (arr[centre] > arr[r]) swap(arr[centre], arr[r]);
    swap(arr[centre], arr[l]);
    return arr[l];
  }

  int partition(vector<int>& arr, int lo, int hi) {
    int pivot = median3(arr, lo, hi);
    int i = lo+1, j = hi;
    while (i <= j) {
      while (i <= hi && arr[i] <= pivot) i += 1;
      if (i > j) break;
      while (j > lo && arr[j] >= pivot) j -= 1;
      if (i > j) break;
      swap(arr[i], arr[j]);
    }
    swap(arr[lo], arr[j]);
    return j;
  }
};
