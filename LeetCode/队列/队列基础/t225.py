from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        ans = self.q1.popleft()

        self.q1, self.q2 = self.q2, self.q1

        return ans

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        ans = self.q1.popleft()
        self.q2.append(ans)

        self.q1, self.q2 = self.q2, self.q1

        return ans

    def empty(self) -> bool:
        return len(self.q1) == 0


class MyStack1:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1


class MyStack2:

    def __init__(self):
        self.deque = deque()

    def push(self, x: int) -> None:
        self.deque.append(x)
        for _ in range(len(self.deque) - 1):
            self.deque.append(self.deque.popleft())

    def pop(self) -> int:
        return self.deque.popleft()

    def top(self) -> int:
        return self.deque[0]

    def empty(self) -> bool:
        return not self.deque
