### 스택 자료구조
+ 먼저 들어 온 데이터가 나중에 나가는 형식
+ 입구와 출구가 동일한 형태

```python
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력   [1, 3, 2, 5]
print(stack) # 최하단 원소부터 출력  [5, 2, 3, 1]
```
```c++
stack<int> s;

int main(void) {
    s.push(5);
    s.push(2);
    s.push(3);
    s.push(7);
    s.pop();
    s.push(1);
    s.push(4);
    s.pop();
    
    // 스택의 최상단 원소부터 출력
    while (!s.empty()) {
        cout << s.top() << ' ';
        s.pop();
    }
}

// 결과: 1, 3, 2, 5
```
### 큐 자료구조
+ 먼저 들어 온 데이터가 먼저 나가는 형식
+ 입구와 출구가 모두 뚫려 있는 터널과 같은 형태

```python
from colletions import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)    # 먼저 들어온 순서대로  deque([3, 7, 1, 4])
queue.reverse()
print(queue)    # 나중에 들어온 원소부터 deque([4, 1, 7, 3])
```

```c++
queue<int> q;

int main(void) {
    q.push(5);
    q.push(2);
    q.push(3);
    q.push(7);
    q.pop();
    q.push(1);
    q.push(4);
    q.pop();
    
    // 먼저 들어온 원소부터 출력
    while (!s.empty()) {
        cout << q.front() << ' ';
        s.pop();
    }
}
```

### 재귀 함수
+ 재귀 함수는 자기 자신을 다시 호출하는 함수를 의미한다.
+ 재귀 함수의 종료 조건을 꼭 명시해야 함

```python
def factorial(n):
    if (n <= 1):
        return 1
    return n * factorial(n-1)
```

# DFS
+ DFS는 깊이 우선 탐색이라고도 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.
+ DFS는 스택 자료구조(혹은 재귀 함수)를 이용하며, 구체적인 동작 과정은 다음과 같다.
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 더 이상 2번 과정을 수행할 수 없을 때까지 반복한다.

### DFS 동작 예시 
