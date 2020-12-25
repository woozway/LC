class MyQueue:
  def __init__(self):
    self.s1 = []
    self.s2 = []
    self.front = None

  def push(self, x: int) -> None:
    if not self.s1: self.front = x
    self.s1.append(x)

  def pop(self) -> int:
    if not self.s2:
      while self.s1:
        self.s2.append(self.s1.pop())
      self.front = None
    return self.s2.pop()

  def peek(self) -> int:
    return self.s2[-1] if self.s2 else self.front

  def empty(self) -> bool:
    return not self.s1 and not self.s2
