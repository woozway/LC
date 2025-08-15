class Solution {
public:    
  int minMutation(string startGene, string endGene, vector<string>& bank) {
    if (startGene == endGene) return 0;

    unordered_set<string> S;
    for (auto &w : bank) S.insert(w);
    if (!S.count(endGene)) return -1;

    string keys = "ACGT";
    unordered_set<string> st; // st记录str是否访问过
    queue<string> q;
    q.push(startGene), st.insert(startGene);
    int step = 1;
    while (q.size()) {
      int n = q.size();
      while (n -- ) {
        auto t = q.front(); q.pop();
        for (int i = 0; i < 8; i ++ )
          for (int j = 0; j < 4; j ++ )
            if (keys[j] != t[i]) {
              string nxtGene = t;
              nxtGene[i] = keys[j];
              if (!st.count(nxtGene) && S.count(nxtGene)) {
                if (nxtGene == endGene) return step;
                q.push(nxtGene), st.insert(nxtGene);
              }
            }
      }
      step ++ ;
    }
    return -1;
  }
};