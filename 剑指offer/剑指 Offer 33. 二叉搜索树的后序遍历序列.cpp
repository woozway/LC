// recursion
// T=O(n)
// S=O(lgn)

class Solution {
public:
  bool verifyPostorder(vector<int>& postorder) {
    return check(postorder, 0, postorder.size()-1);
  }

  bool check(vector<int>& postorder, int lo, int hi) {
    if (lo > hi) {
      return true;
    }
    int rootVal = postorder[hi];
    int index = lo;
    while (index<hi && postorder[index]<rootVal) {
      index += 1;
    }
    if (hi-1-index+1>0 && getMin(postorder, index, hi-1)<rootVal) {
      return false;
    }
    return check(postorder, lo, index-1) && check(postorder, index, hi-1);
  }

  int getMin(vector<int>& a, int lo, int hi) {
    int minVal = INT_MAX;
    for (int i = lo; i <= hi; i++) {
      minVal = min(minVal, a[i]);
    }
    return minVal;
  }
};
