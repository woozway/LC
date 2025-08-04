class Solution {
public:
  int search(vector<int>& nums, int target) {
    int n = nums.size();
    auto &a = nums;

    // 确定a[mid]和target的左右关系
    int l = 0, r = n - 1;
    while (l < r) {
      int mid = l + r >> 1; // 更新方式无所谓，若改成l+r+1>>1，对应l和r也要改成mid和mid+1
      if (a[mid] > a[r] && target <= a[r]) l = mid + 1; // a[l~mid]有序，分两段，mid在左段，target在右段
      else if (a[mid] <= a[r] && target > a[r]) r = mid - 1; // a[mid~r]有序，mid在右段，target在左段
      else { // target和mid在同一递增段，分成两部分：(...,), (k, ...)
        if (a[mid] < target) l = mid + 1;
        else r = mid;
      }
    }
    
    if (a[l] == target) return l;
    return -1;
  }
};