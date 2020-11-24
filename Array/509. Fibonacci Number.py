class Solution:
  def fib(self, N: int) -> int:
    """
    T=O(1), S=O(1), Binet's formula
    """
    golden_ratio = (1 + 5 ** 0.5) / 2
    return int((golden_ratio ** N + 1) / 5 ** 0.5)
