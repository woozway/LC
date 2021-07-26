// binary search II
// T=O(n) in worst case, T=O(lgn) in average case
// S=O(1)

class Solution {
public:
  int minArray(vector<int>& numbers) {
    int lo = 0, hi = numbers.size()-1;
    while (lo < hi) {
      int mid = lo + (hi-lo)/2;
      if (numbers[mid] < numbers[hi]) {
        hi = mid;
      } else if (numbers[mid] > numbers[hi]) {
        lo = mid + 1;
      } else {
        hi--;
      }
    }
    return numbers[lo];
  }
};