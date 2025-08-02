class Solution {
public:
  int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
    int res = 0;
    int min_s = 0, s = 0;
    for (int i = 0; i < gas.size(); i ++ ) {
      s += gas[i] - cost[i];
      if (s < min_s) {
        min_s = s;
        res = i + 1;
      }
    }

    if (s < 0) return -1;
    else return res;
  }
};