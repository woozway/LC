const int INF = 1e9;

class Solution {
public:
  double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    if (nums1.size() > nums2.size()) return findMedianSortedArrays(nums2, nums1);
    
    auto &a = nums1, &b = nums2;
    int n1 = a.size(), n2 = b.size();
    
    int med1 = -INF, med2 = -INF; // median1：前一部分的最大值，median2：后一部分的最小值
    int l = 0, r = n1;
    while (l <= r) {
      int i = l + r >> 1; // 前一部分包含 a[0 ~ i-1] 和 b[0 ~ j-1]
      int j = (n1 + n2 + 1) / 2 - i; // 后一部分包含 a[i ~ n1-1] 和 b[j ~ n2-1]

      // a_i_1, a_i, b_j_1, b_j 分别表示 a[i-1], a[i], b[j-1], b[j]
      int a_i_1 = (!i ? -INF : a[i - 1]);
      int a_i = (i == n1 ? INF : a[i]);
      int b_j_1 = (!j ? -INF : b[j - 1]);
      int b_j = (j == n2 ? INF : b[j]);

      if (a_i_1 > b_j) r = i - 1;
      else {
        med1 = max(a_i_1, b_j_1);
        med2 = min(a_i, b_j);
        l = i + 1;
      }
    }

    return (n1 + n2) % 2 == 0 ? (med1 + med2) / 2.0 : med1;
  }
};