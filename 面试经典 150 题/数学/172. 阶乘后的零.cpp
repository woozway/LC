class Solution {
  unordered_map<int, int> primes;

public:
  int trailingZeroes(int n) {
    if (!n) return 0;

    for (int j = 1; j <= n; j ++ ) {
      int a = j;
      for (int i = 2; i <= a / i; i ++ )
        if (a % i == 0)
          while (a % i == 0) a /= i, primes[i] ++ ;
      if (a > 1) primes[a] ++ ;
    }
    return min(primes[2], primes[5]); // 2*5=10
  }
};