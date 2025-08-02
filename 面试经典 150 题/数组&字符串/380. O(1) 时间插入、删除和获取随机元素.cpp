class RandomizedSet {
  unordered_map<int, int> h; // 记录val在数组a中的位置
  vector<int> a;

public:
  RandomizedSet() {
    
  }
  
  bool insert(int val) {
    if (h.count(val)) return false;

    h[val] = a.size();
    a.push_back(val);
    return true;
  }
  
  bool remove(int val) {
    if (!h.count(val)) return false;

    h[a.back()] = h[val];
    a[h[val]] = a.back();
    h.erase(val);
    a.pop_back();
    return true;
  }
  
  int getRandom() {
    return a[rand() % a.size()];
  }
};