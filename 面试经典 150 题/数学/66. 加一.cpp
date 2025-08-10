class Solution {
  vector<int> add(vector<int> &A, vector<int> &B) { // C=A+B, A>=0, B>=0
    if (A.size() < B.size()) return add(B, A);

    vector<int> C;
    int t = 0;
    for (int i = 0; i < A.size(); i ++ ) {
      t += A[i]; // 进位
      if (i < B.size()) t += B[i];
      C.push_back(t % 10);
      t /= 10;
    }
    if (t) C.push_back(t);

    return C;
  }

public:
  vector<int> plusOne(vector<int>& digits) {
    vector<int> A = digits, B = {1}; // 由低到高倒着存，方便加减运算
    reverse(A.begin(), A.end());
    
    auto C = add(A, B);
    reverse(C.begin(), C.end());
    
    return C;
  }
};