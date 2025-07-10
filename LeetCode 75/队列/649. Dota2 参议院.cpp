class Solution {
public:
  string predictPartyVictory(string senate) {
    int n = senate.size();
    auto &s = senate;

    queue<int> r, d;
    for (int i = 0; i < n; i ++ )
      if (s[i] == 'R') r.push(i);
      else d.push(i);
    
    while (r.size() && d.size()) {
      if (r.front() < d.front()) r.push(r.front() + n);
      else d.push(d.front() + n);
      r.pop();
      d.pop();
    }
    
    if (r.size()) return "Radiant";
    else return "Dire";
  }
};